from typing import BinaryIO
from MenuServices import *
from Player import *
from gestionScore import *
import os
import time

if __name__ == "__main__":
    player1: player = player()
    player2: player = player()

    player_init(player1,player2)                   #Vérification que les deux nom saisies ne sont pas identiques et initialisation des scores à 0
    find_existing_player_and_increment_score(player1,"tout",0) #L'option tout permet s'adresse au joueur ayant déjà joueur le permettant de récuupérer leur score. De ce fait le nombre de point à augmenter est de 0.
    find_existing_player_and_increment_score(player2,"tout",0)
    write_score_folder(player1)     #La procédure précédente retire du fichier carnet.dat le joueur en question avec ses scores. Cette procédure ajoute le joueur dans le fichier avec ses nouveaux scores qui correspondent à ses anciens.           
    write_score_folder(player2)

    #Sert exclusivement pour la suppression du fichier carnet.dat permit par l'administrateur.
    main_menu_choice: int = 0
    while main_menu_choice !=4 :

        while main_menu_choice != 4: 
            #Nettoie le terminal
            os.system('cls' if os.name == 'nt' else 'clear')       
            display_main_menu()
            try:
                main_menu_choice = int(input("\n Saisissez ce à quoi vous voulez accéder : "))

                match int(main_menu_choice):

                    case 1:
                        manage_games_menu(player1, player2)
                
                    case 2:
                        manage_score_menu(player1, player2)

                    case 3: 
                        display_score_history()

                    case 4:
                        remove_player_if_not_playing()

                    case _:
                        print("\n\n erreur de saisie")
                        time.sleep(1)

                break
        
            except ValueError:
                print("Veuillez saisir un nombre valide.")
                time.sleep(1)

print("Au revoir")