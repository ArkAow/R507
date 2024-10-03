import pytest
import pickle
from unittest import mock
from Player import player  # Suppose que Player est bien défini dans ce module
from gestionScore import (
    display_score_history, write_score_folder,
    find_existing_player_and_increment_score, 
    display_playing_players_score, ranking_per_game, 
    ranking_player_total_score, remove_player_if_not_playing, 
    delete_score_folder
)

# Mocking necessary functions and data
folder_name = "carnet.dat"

@pytest.fixture
def mock_player():
    """Fixture to create a mock player for the tests."""
    p = player()
    p.name = "Player1"
    p.score = mock.Mock()
    p.score.score_tic_tac_toe = 10
    return p

def test_display_score_history(mock_player):
    """Test for the display_score_history function when the file exists."""
    with mock.patch("builtins.open", mock.mock_open(read_data=pickle.dumps(mock_player))), \
         mock.patch("pickle.load", side_effect=[mock_player, EOFError]), \
         mock.patch("builtins.input", return_value="q"):

        display_score_history()

def test_display_score_history_file_not_found():
    """Test for the display_score_history function when the file doesn't exist."""
    with mock.patch("builtins.open", side_effect=FileNotFoundError):
        display_score_history()

def test_write_score_folder(mock_player):
    """Test for the write_score_folder function."""
    with mock.patch("builtins.open", mock.mock_open()) as mock_file:
        write_score_folder(mock_player)
        mock_file.assert_called_once_with(folder_name, "ab")
        mock_file().write.assert_called()

def test_find_existing_player_and_increment_score(mock_player):
    """Test for the find_existing_player_and_increment_score function."""
    mock_player2 = mock.Mock()
    mock_player2.name = "Player2"
    mock_player2.score.score_tic_tac_toe = 5

    with mock.patch("builtins.open", mock.mock_open(read_data=pickle.dumps(mock_player))), \
         mock.patch("pickle.load", side_effect=[mock_player, EOFError]):

        find_existing_player_and_increment_score(mock_player2, "TICTACTOE", 5)
        assert mock_player2.score.score_tic_tac_toe == 10  # 5 initial + 5 increment

def test_display_playing_players_score(mock_player):
    """Test for the display_playing_players_score function."""
    mock_player2 = mock.Mock()
    mock_player2.name = "Player2"
    mock_player2.score.score_tic_tac_toe = 15

    with mock.patch("builtins.open", mock.mock_open(read_data=pickle.dumps(mock_player))), \
         mock.patch("pickle.load", side_effect=[mock_player, EOFError]), \
         mock.patch("builtins.input", return_value="q"):

        display_playing_players_score(mock_player, mock_player2)

def test_ranking_per_game(mock_player):
    """Test for the ranking_per_game function."""
    with mock.patch("builtins.open", mock.mock_open(read_data=pickle.dumps(mock_player))), \
         mock.patch("pickle.load", side_effect=[mock_player, EOFError]), \
         mock.patch("builtins.print") as mock_print:

        ranking_per_game("TICTACTOE")
        mock_print.assert_any_call(mock_player.name, ":", mock_player.score.score_tic_tac_toe, " points")

def test_ranking_player_total_score(mock_player):
    """Test for the ranking_player_total_score function."""
    with mock.patch("builtins.open", mock.mock_open(read_data=pickle.dumps(mock_player))), \
         mock.patch("pickle.load", side_effect=[mock_player, EOFError]), \
         mock.patch("builtins.print") as mock_print, \
         mock.patch("builtins.input", return_value="q"):

        ranking_player_total_score()
        mock_print.assert_any_call(mock_player.name, " à un score total de : ", str(mock_player.score.score_tic_tac_toe), " points")

def test_remove_player_if_not_playing(mock_player):
    """Test for the remove_player_if_not_playing function."""
    mock_player.score.score_tic_tac_toe = 0  # Simulate that player has never played
    mock_player2 = mock.Mock()
    mock_player2.score.score_tic_tac_toe = 15

    with mock.patch("builtins.open", mock.mock_open(read_data=pickle.dumps(mock_player))), \
         mock.patch("pickle.load", side_effect=[mock_player, mock_player2, EOFError]), \
         mock.patch("pickle.dump") as mock_dump:

        remove_player_if_not_playing()
        # Only the player who played should be dumped
        mock_dump.assert_called_once_with(mock_player2, mock.ANY)

def test_delete_score_folder():
    """Test for the delete_score_folder function."""
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("os.remove") as mock_remove, \
         mock.patch("builtins.input", side_effect=["MesriCharpentierBUT1", "Y"]):

        delete_score_folder()
        mock_remove.assert_called_once_with(folder_name)
