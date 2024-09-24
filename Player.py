class score:
    score_tic_tac_toe:int
    
class player:
    name:str
    score:score
    order:int
    symbole:str

def player_init(player1: player, player2: player):
    """Cette procédure permet d'initialité les pseudo des joueurs et d'initialisé leur score à 0
        pré-condition : deux joueurs de type joueur
        post-conditon : les deux joueurs de type joueur """
    
    player1.score = score()
    player1.score.score_tic_tac_toe = 0

    player2.score = score()
    player2.score.score_tic_tac_toe = 0

    print("####################################")
    print("|      CONNEXION                   |")
    print("------------------------------------")
    player1.name = input("\nVeulliez saisir le nom du joueur1 : ")
    player2.name = input("\nVeulliez saisir le nom du joueur2 : ")
    while player1.name == player2.name:

        print("Vous ne pouvez pas avoir le même pseudo !")
        player1.name = input("\nVeulliez saisir le nom du joueur1 : ")
        player2.name = input("\nVeulliez saisir le nom du joueur2 : ")
