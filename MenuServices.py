from Player import *
from TicTacToe import *

tictactoe_rules = "\n Chaque joueur pose sa marque (un O ou un X) à tour de rôle dans les case d'une grille de 3x3.\nLe premier qui aligne 3 marques a gagné."

def display_main_menu():

    """Procédure qui affiche un menu principal
        pré-condition : rien
        post-condition : rien"""

    print("#########################################")
    print("|         MENU PRINCIPAL                |")
    print("|------------------------------------   |")
    print("| 1 - Les jeux                          |")
    print("| 2 - Les scores                        |")
    print("| 3 - Afficher historique des parties   |")
    print("| 4 - Quitter                           |")
    print("#########################################")

def display_game_menu():

    """Procédure qui affiche un menu pour les jeux.
        pré-condition : rien
        post-condition : rien"""

    print("######################")
    print("|     THE GAMES      |")
    print("----------------------")
    print("| 1 - Morpion        |")
    print("| 2 - Quitter        |")
    print("######################")

def display_score_menu():

    """Procédure qui affiche un menu pour les scores.
        pré-condition : rien
        post-condition : rien"""

    print("############################################")
    print("|                   SCORE                  |")
    print("--------------------------------------------")
    print("| 1 - Afficher les scores joueurs connectés|")
    print("| 2 - Afficher le classement par jeux      |")
    print("| 3 - Afficher le classement par score     |")
    print("| 4 - Supprimer fichier des scores (admin) |")
    print("| 5 - Quitter                              |")
    print("############################################")

def display_rules_menu(regleDuJeu : str):

    """Cette procédure permet d'afficher les règle du jeu en question si les joueurs le veuillent ou non.
        pré-condition : une chaîne de caractère contenant la règle du jeu
        post-condition : rien"""
    
    end_rule_display: bool = False
    rule_choice: str = input("\nVoulez-vous un rappel des règles (Y/n) ? --> ")
    if rule_choice.capitalize() == "Y":

        while not end_rule_display:

            print(regleDuJeu)
            temp = input("\nEntrer ce que vous voulez pour quitter le rappel des règles : ")
            end_rule_display = True

def manage_games_menu(player1: int, player2: int):

    game_menu_choice = 0
    while game_menu_choice != 5:
        
        os.system('cls' if os.name == 'nt' else 'clear')  
        display_game_menu()
        try:
            game_menu_choice = int(input("\nSaisissez à quel jeu vous voulez jouer : "))
            match game_menu_choice:

                case 1:
                    display_rules_menu(tictactoe_rules)
                    Morpion(player1, player2)

                case 2:
                    break

                case _:
                    print("\n\nerreur de saisie")
                    time.sleep(1)

        except ValueError:
                print("Veuillez saisir un nombre valide.")
                time.sleep(1)

def manage_score_menu(player1: int, player2: int):

    score_menu_choice = 0
    while score_menu_choice != 5:

        os.system('cls' if os.name == 'nt' else 'clear')
        display_score_menu()
        try:
            score_menu_choice = int(input("\nSaisissez ce que vous voulez faire : "))
            match score_menu_choice:

                case 1:
                    display_playing_players_score(player1,player2)

                case 2:
                    ranking_per_game("Morpion")
                    temp = input("Entrer ce que vous voulez pour sortir de cet affichage : ")

                case 3:
                    ranking_player_total_score()

                case 4:
                    delete_score_folder()
                    
                case 5:
                    break

                case _:
                    print("\n\nerreur de sais5e")
                    time.sleep(1)
                    
        except ValueError:
                print("Veuillez saisir un nombre valide.")
                time.sleep(1)