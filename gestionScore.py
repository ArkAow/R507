from typing import BinaryIO
import pickle
from Player import *
import time
import os

folder_name: str = "carnet.dat"

def display_score_history():
    """Cette procédure permet d'afficher l'historique des parties du plus anciens au plus récent. L'historique comprend le nom et le score des jeux de chaques joueur dans le fichier.
        pré-condition : un fichier 'carnet.dat' qui existe.
        post-condtion: rien """

    try:

        folder = open(folder_name,"rb")
        is_quitting: bool = False
        while not is_quitting:

            folder = open("carnet.dat","rb")
            finished: bool = False
            p: player = player()
            while not finished:

                try :

                    p = pickle.load(folder)
                    print("Pseudo : ",p.name)
                    print("score du jeu Morpion : ", p.score.score_tic_tac_toe)
                    print(" ")

                except EOFError :

                    finished = True

            folder.close()
            temp = input("Entrer ce que vous voulez pour quitter cet affichage : ")
            is_quitting = True

    except FileNotFoundError:

        print("Il n'y a pas encore eu de partie soyez les premiers à jouer !")
        time.sleep(2)

def write_score_folder(p: player):
    """Cette procédure permet d'ajouter des joueurs dans le fichier carnet.dat. Si il n'existe pas on le créer.
        pré-condition : un joueur.
        post-condition : un fichier contenant le joueur."""
    
    folder = open(folder_name,"ab")
    pickle.dump(p,folder)
    folder.close()

def find_existing_player_and_increment_score(p: player, option: str, nb_point: int):
    """Cette procédure permet de chercher le score d'un joueur si se joueur à déjà joué et de l'incrémenter en fonction du nombre de points du jeu.
        pré-condition : un joueur, une option corréspondant à l'indication du nom du jeu, le nombre de point du jeu en option qui est en entier et un fichier 'carnet.dat' qui existe
        post-condition : un joueur avec son score qui est incrementer et un fichier actualisant le score du joueur en question."""
    
    try:

        folder = open(folder_name,"rb")
        player_list: list[player] = []
        playr: player = player()
        finished: bool = False
        while not finished :

            try :

                playr = pickle.load(folder)
                match option.capitalize():

                    case "ALL":

                        if playr.name == p.name:

                            p.score.score_tic_tac_toe = playr.score.score_tic_tac_toe

                        else:

                            player_list.append(p)

                    case "TICTACTOE":

                        if playr.name == p.name:

                            p.score.score_tic_tac_toe += nb_point

                        else:

                            player_list.append(p)

            except EOFError :

                finished = True
    
        folder.close()
        folder = open("carnet.dat","wb")
        for i in range(len(player_list)):

            pickle.dump(player_list[i],folder)

        folder.close()

    except FileNotFoundError:

        print("Erreur lors de la lecture du fichier")
        time.sleep(2)
 
def display_playing_players_score(p1: player, p2: player):
    """Cette procédure permet d'afficher les scores des deux joueurs qui sont an train de lancer l'application.
        pré-condition : deux joueurs de type joueur et un fichier qui existe.
        post-condition : rien"""
    
    try:

        folder = open(folder_name,"rb")
        p: player = player()
        finished: bool = False
        is_quitting: bool = False
        player_name_list: list[str] = []
        while not is_quitting:

            while not finished:

                try : 

                    p = pickle.load(folder)
                    if p.name == p1.name:

                        print("Pseudo : ",p.name)
                        print("score du jeu Morpion : ", p.score.score_tic_tac_toe)
                        print("")

                    elif p.name == p2.name:

                        print("Pseudo : ",p.name)
                        print("score du jeu Morpion : ", p.score.score_tic_tac_toe)
                        print("")

                    player_name_list.append(p.name)

                except EOFError:

                    finished = True

                folder.close

            if p1.name not in player_name_list:

                print("Pseudo : ",p1.name)
                print("score du jeu Morpion : ", 0)
                print("")

            if p2.name not in player_name_list:

                print("Pseudo : ",p2.name)
                print("score du jeu Morpion : ", 0)
                print("")

            temp = input("Entrer ce que vous voulez pour quitter -> ")
            is_quitting = True

    except FileNotFoundError:

        print("Pseudo : ",p1.name)
        print("score du jeu Morpion : ", 0)
        print(" ")
    
        print("Pseudo : ",p2.name)
        print("score du jeu Morpion : ", 0)
        print(" ")
        time.sleep(2)

def score_sorting(score_list: list[int], name_list: list[str]):
    """Cette procédure permet de trier les scores (plus petit-> premier élément du tableau) et change la position du détenteur du score en fonction de son score.
        pré-condition : une liste d'entiers et une liste de chaînes
        post-condition : une liste d'entiers triés et une liste de chaînes triées en fonction de leur score."""
    
    k: int
    i: int
    j: int
    val1: int
    val2: int
    
    k = len(score_list)
    for i in range(k):
        val = score_list[i]
        val2 = name_list[i]
        j=i
        while j>0 and score_list[j-1]>val:
            score_list[j] = score_list[j-1]
            name_list[j] = name_list[j-1]
            j-=1
        score_list[j] = val
        name_list[j] = val2

def ranking_per_game(game_name: str):
    """Cette procédure permet afficher le score de chaque joueur en fonction du jeu passé en paramètre par ordre décroissant
        pré-condition : une chaîne de caractère et un fichier qui existe
        post-condition : rien"""
 
    folder: BinaryIO
    try:

        folder = open(folder_name,"rb")
        p: player = player()
        finished: bool = False
        score_list: list[int] = []
        name_list: list[str] = []
        while not finished:

            try:

                p = pickle.load(folder)
                match game_name.capitalize():

                    case "TICTACTOE":
                      
                      score_list.append(p.score.score_tic_tac_toe)

                name_list.append(p.name)

            except EOFError:

                finished = True

        folder.close()
        score_sorting(score_list,name_list)
        index : int
        index = len(score_list)-1
        print("Classement pour ",game_name," : ")
        while index>-1:

            print(name_list[index], ":",score_list[index]," points")
            index-=1

        print("")

    except FileNotFoundError:

        print("Il n'y a pas encore eu de partie soyez les premiers à jouer !")
        time.sleep(2)

def ranking_player_total_score():
    """Cette procédure permet d'afficher le score total des quatres jeux de chaque joueur par ordre décroissant.
       pré-condition : il faut que le fichier existe
       post-condition : rien """
    
    folder: BinaryIO
    try:

        is_quitting: bool = False
        score_list: list[int] = []
        name_list: list[str] = []
        folder = open(folder_name,"rb")
        p: player = player()
        finished: bool = False
        
        while not finished:

            try:

                total_score: int = 0
                p = pickle.load(folder)
                total_score = p.score.score_tic_tac_toe
                name_list.append(p.name)
                score_list.append(total_score)

            except EOFError:

                finished = True
            
        score_sorting(score_list,name_list)
        while not is_quitting:

            for i in range(len(name_list)):

                print(name_list[i]," à un score total de : ",str(score_list[i])," points")

            temp = input("Entrer ce que vous voulez pour quitter cet affichage : ")
            is_quitting = True

    except FileNotFoundError:

        print("Il n'y a pas encore eu de partie soyez les premiers à jouer !")
        time.sleep(2)

def remove_player_if_not_playing():
    """Cette procédure permet de vérifier si un joueur à jouer ou pas et de le supprimer.
        De plus, on considère que si le joueur n'a jamais gagné de point c'est comme si il n'avais pas jouer et on le supprime
        pré-condition : un fichier qui existe
        post-condition : un fichier ne contenant que les joueurs ayant au moins un score > 0 sur l'un des jeux """
    
    folder : BinaryIO
    try:

        folder = open(folder_name,"rb")
        p: player = player()
        player_who_have_played: list[player] = []
        finished: bool = False
        while not finished:

            try:

                p = pickle.load(folder)
                if p.score.score_tic_tac_toe > 0:
                    player_who_have_played.append(p)

            except EOFError:

                finished = True

        folder.close()
        folder = open(folder_name,"wb")
        for i in range(len(player_who_have_played)):

            pickle.dump(player_who_have_played[i],folder)

        folder.close()

    except FileNotFoundError:

        pass

def delete_score_folder():
    """Cette procédure permet de supprimer le fichier des scores. La suppression du fichier implique l'arrêt du programme.
        pré-condition : il faut que le fichier existe pour pouvoir le supprimer, et un booléen qui permettra d'arreter le programme si on supprime le fichier.
        post-condition : supprime un fichier si il existe et renvoie un booléen"""
    
    folder: BinaryIO
    try:

        folder = open(folder_name,"rb")
        folder.close()
        delete_password: str = input("Entrer le mot de passe administrateur pour pouvoir supprimer le fichier des scores : ")
        if delete_password == "MesriCharpentierBUT1":

            attention:str = input("\nLa suppréssion du fichier nécessite un arrêt de l'application. De plus tous les scores seront supprimés.\nEtes-vous sur ? (Y/n) -> ")
            if attention.capitalize == "Y":

                os.remove(folder_name)
                print("Le fichier à bel est bien était supprimer l'application va s'arreter.")
                time.sleep(2)
                exit()

        else:

            print("Vous ne pouvez pas supprimer le fichier des scores.")
            time.sleep(2)

    except FileNotFoundError:

        print("Le fichier des scores n'existe pas.")
        time.sleep(2)
