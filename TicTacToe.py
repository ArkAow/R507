import os
from Player import *
from gestionScore import * 

def creation_matrice()->list[list[str]]:
    """Cette Procédure me permet de créer un tableau à 2 dimensions avec 3 lignes et trois colonnes pour le plateau du morpion.
       L'affichage de cette matrice sera modifiée plus tard dans le programme pour avoir un rendu visuel du jeu agréable.
       pré-condition : rien 
       post-Condtion : une matrice de chaîne """
    i : int
    j : int
    val : str
    mat : list[list[str]]
    mat = list([])

    for i in range (0,3):
        ligne : list[str]
        ligne = list()
        for j in range(0,3):
            val = "- "
            ligne.append(val)
        mat.append(ligne)
    return mat

def affichageMatrice(mat : list[list[str]]):
    """Cette procédure permet d'afficher une matrice de chaîne en plateau morpion.
       Pré-condtion : une matrice de chaîne qui sera modifiée à chaque appel de la fonction en remplaçant les chaînes de caractères par les symboles du morpion.
       Post-condition : rien."""
    
    ch : str
    print(" ")
    for i in range(3):

        if mat[i][0] == "X" or mat[i][0] =="O":
            ch = " "
        else:
            ch = ""
        print(" ",mat[i][0],ch," | ",end="")

        if mat[i][1] == "X" or mat[i][1] =="O":
            ch = " "
        else:
            ch = ""
        print(" ",mat[i][1],ch," | ",end="")
        print(" ",mat[i][2])
        if i<2 and len(mat[i][0])!=3:
            print("-------|--------|-------")
        elif i<2 and len(mat[i][0])==3:
            print("--------|---------|-------")
        else:
            print("")
            
def creationCoordonneeplateau()->list[list[str]]:
    """Cette procédure créer une matrice de chaîne avec les coordonées du plateau du jeu converti en chaîne de caractères.
        pré-condition : rien
        post-concdition : une matrice de chaîne"""
    i : int
    j : int
    val : str
    mat : list[list[str]]
    mat = list([])

    for i in range (0,3):
        ligne : list[str]
        ligne = list()
        for j in range(0,3):
            val = str(i)+"/"+str(j)
            ligne.append(val)
        mat.append(ligne)
    return mat

def verificationX(aX : int)->int:
    """Cette fonction me permet de vérifier que les utilisateurs rentre des abscisses valides (0,1 ou 2).
       Pré-condition : prend comme paramètre un entier.
       Post-conditon : renvoie un entier compris entre 0 et 2 (inclus)."""
    while aX<0 or aX>2:
        if aX<0 or aX>2:
            aX = int(input("L'abscisse doit être comprise entre 0 et 2  : "))
    return aX

def verificationY(cY : int)->int:
    """Cette fonction me permet de vérifier que les utilisateurs rentre des ordonnées valides (0,1 ou 2).
       Pré-condition : prend comme paramètre un entier.
       Post-conditon : renvoie un entier compris entre 0 et 2 (inclus)."""
    while cY<0 or cY>2:
        if cY<0 or cY>2:
            cY = int(input("L'ordonné doit être comprise entre 0 et 2 : "))
    return cY
        
def conditionWin(mat : list[list[str]], signe : str)-> bool:
    """Cette fonction permet de vérifier les condtions pour gagner au morpion en fonction du signe.
       Pré-condition : prend comme paramètres la matrice du jeu avec le signe du joueur 1 ou 2.
       Post-condition : renvoie un booléen indiquant si les conditions requises pour gagner du joueur 1 ou 2 sont remplies.
    """
    if (mat[0][0] == signe and mat[0][1] == signe and mat[0][2] == signe):
        return True
    if (mat[1][0] == signe and mat[1][1] == signe and mat[1][2] == signe):
        return True
    if (mat[2][0] == signe and mat[2][1] == signe and mat[2][2] == signe):
        return True
    if (mat[0][0] == signe and mat[1][0] == signe and mat[2][0] == signe):
        return True
    if (mat[0][1] == signe and mat[1][1] == signe and mat[2][1] == signe):
        return True
    if (mat[0][2] == signe and mat[1][2] == signe and mat[2][2] == signe):
        return True
    if (mat[0][0] == signe and mat[1][1] == signe and mat[2][2] == signe):
        return True
    if (mat[0][2] == signe and mat[1][1] == signe and mat[2][0] == signe):
        return True

def play(joueurTour : player ,matriceCoordonne : list[list[str]],matrice : list[list[str]],game : bool)->bool:
    """Cette fonction permet de lancer le jeux morpion à tour de rôle entre le joueur 1 et 2
        pré-condition : le joueur en question, la matrice des coordonnées  et la matrice du plateau du jeu, le booléen
        game qui va permettre de savoir lorsque qu'un joueur à gagner pour arreter la partie ou si le nombre de tour est atteint.
        post-condition : renvoie un booléen pour savoir si dans le programme principale on continue à appeler la fonction pour jouer.
        Donc si personne n'a encore gagner ou si toutes les cases ne sont pas encore prises."""
    absX : int
    cordY : int

    print("\nVoici les coordonnées du plateau abscisse/ordonnée")
    affichageMatrice(matriceCoordonne)
    affichageMatrice(matrice)
    print(str(joueurTour.name)+" votre symbole est : "+str(joueurTour.symbole))
    #verification des abscisses et ordonnées saisis
    absX = int(input("choisir abscisse : "))
    absX = verificationX(absX)
    cordY = int(input("Choisir ordonnée :"))
    cordY = verificationY(cordY)

    if matrice[absX][cordY] != "X" and matrice[absX][cordY] != "O":  

        matrice[absX][cordY] = joueurTour.symbole #ajoute la marque du joueur dans la matrice à la position souhaité.
        matriceCoordonne[absX][cordY] = "---"

        if conditionWin(matrice,joueurTour.symbole):
            os.system('CLS' if os.name == 'nt' else 'clear')
            if (matrice[0][0]==joueurTour.symbole and matrice[1][1]==joueurTour.symbole and matrice[2][2]==joueurTour.symbole) or (matrice[2][0]==joueurTour.symbole and matrice[1][1]==joueurTour.symbole and matrice[0][2]==joueurTour.symbole):
                #Bonus si le joueur gagne en diagonale
                print("\n"+str(joueurTour.name)+" à gagné en diagonale bonus de 5 points!!")
                find_existing_player_and_increment_score(joueurTour,"Morpion",5) #augmentation score du joueur, mais n'est plus dans le fichier.
                write_score_folder(joueurTour)#on réajoute le joueur dans le fichier avec son score Morpion incrémenter.
            else:
                print("\n"+str(joueurTour.name)+" à gagné !!")
                find_existing_player_and_increment_score(joueurTour,"Morpion",3)
                write_score_folder(joueurTour)
            affichageMatrice(matrice)
            game = False
    else: #si le joueur une case déjà prise par une marque.
        while matrice[absX][cordY] == "X" or matrice[absX][cordY] == "O": #re-demande la saisie de nouvelles coordonnées tant que les coordonnées saisie sont celles d'une case marquer.
            print("\nla case est déjà remplie il est impossible de placer un pion à cette position : ")
            print("\nVoici les coordonnées du plateau abscisse/ordonnée")
            affichageMatrice(matriceCoordonne)
            affichageMatrice(matrice)
            print(str(joueurTour.name)+" votre symbole est : "+str(joueurTour.symbole))
            absX = int(input("choisir abscisse : "))
            absX = verificationX(absX)
            cordY = int(input("Choisir cordonnée :"))
            cordY = verificationY(cordY)

        matrice[absX][cordY] = joueurTour.symbole
        matriceCoordonne[absX][cordY] = "---"

        if conditionWin(matrice,joueurTour.symbole):
            os.system('CLS' if os.name == 'nt' else 'clear')
            if (matrice[0][0]==joueurTour.symbole and matrice[1][1]==joueurTour.symbole and matrice[2][2]==joueurTour.symbole) or (matrice[2][0]==joueurTour.symbole and matrice[1][1]==joueurTour.symbole and matrice[0][2]==joueurTour.symbole):
                #Bonus si le joueur gagne en diagonale
                print("\n"+str(joueurTour.name)+" à gagné en diagonale bonus de 5 points!!")
                find_existing_player_and_increment_score(joueurTour,"Morpion",5)
                write_score_folder(joueurTour)
            else:
                print("\n"+str(joueurTour.name)+" à gagné !!")
                find_existing_player_and_increment_score(joueurTour,"Morpion",3)
                write_score_folder(joueurTour)
            affichageMatrice(matrice)
            game = False
    return game

def Morpion(joueur1 : player,joueur2 : player):
    """Cette procédure permet de lancer le jeu du Morpion et d'y jouer
        pré-condition : deux joueurs de type joueurs
        post-conditions : les deux-joueurs avec leur score modifié dans le fichier carnet.dat"""
    #----------------------------------
    #Initialisation matrice du plateau de jeux
    matrice : list[list[str]]
    matrice = creation_matrice()
    #-----------------------------
    #verife si il y a égalité
    nombreTour : int 
    nombreTour = 0  #Il doit être égale au maximum à 8 car on peut au maximum faire 9 tour.
    #----------------------------
    #Intialisation du la variable game qui va permettre de continuer à jouer au morpion si les conditions sont remplies
    game : bool
    game=True
    #-------------------
    #Permet de définir qui commence. Celui qui commence choisit le signe X ou O.
    debut : int
    os.system('CLS' if os.name == 'nt' else 'clear')
    joueur1.order = int(input("Saisir 1 si "+joueur1.name+" commence sinon saisir 2 si "+joueur2.name+" commence. De plus celui qui commence choisis sa marque (X ou O) : "))
    while joueur1.order <1 or joueur1.order>2:
        joueur1.order = int(input("Saisir 1 si "+joueur1.name+" commence sinon saisir 2 si "+joueur2.name+" commence. De plus celui qui commence choisis sa marque (X ou O) : "))
    os.system('CLS' if os.name == 'nt' else 'clear')
    if joueur1.order == 1:
        debut = 0
        joueur1.symbole = input(str(joueur1.name)+" Saisir X ou O selon le symbole que vous désirez : ")
        while joueur1.symbole != "X" and joueur1.symbole !="O":
            joueur1.symbole = input(str(joueur1.name)+" Saisir X ou O selon le symbole que vous désirez : ")
        if joueur1.symbole == "X":
            joueur2.symbole = "O"
        else:
            joueur2.symbole = "X"
    else:
        debut = 1
        joueur2.symbole = input(str(joueur2.name)+" Saisir X ou O selon le symbole que vous désirez : ")
        while joueur2.symbole != "X" and joueur2.symbole !="O":
            joueur2.symbole = input(str(joueur2.name)+" Saisir X ou O selon le symbole que vous désirez : ")
        if joueur2.symbole == "X":
            joueur1.symbole = "O"
        else:
            joueur1.symbole = "X"
    #----------------------------------------------------
    #Initialistatinon de la matrice qui contiendra les coordonnées pour chaque case du plateau du jeu
    matriceCoordonne : list[list[str]]
    matriceCoordonne = creationCoordonneeplateau()
    #--------------------------------------------------
    sortirAffichageScoreMorpion : str
    finAffichageMorpion:bool
    finAffichageMorpion = False
    while not finAffichageMorpion:
        #cette boucle permet de laisser le résulat final du morpion jusqu'a ce que les utilisateurs rentre nimporte quoi pour quitter l'affichage
        while game:
            """Cette boucle permet de joueur au morpion tant que c'est possible donc jusqu'a ce que les cases soit remplies ou que les conditions pour gagner sont réunies"""
            os.system('CLS' if os.name == 'nt' else 'clear') #cette fonction importer du module os permet de rafraichir le terminal
            if nombreTour<=8:#verifie que le nombre de tour ne soit pas supérieur à 10 car il y a 9 cases au morpion donc 9 tours maximum 
                if debut == 0:
                    game = play(joueur1,matriceCoordonne,matrice,game)
                    debut+=1 
                else:
                    game = play(joueur2,matriceCoordonne,matrice,game)
                    debut -=1
                nombreTour+=1
            else:
                print("\n\nIl y a égalité !")
                affichageMatrice(matrice)
                game = False
        
        if joueur1.score.score_tic_tac_toe>joueur2.score.score_tic_tac_toe:
            print("\n ",joueur1.name," à un score de : ",joueur1.score.score_tic_tac_toe," point(s)")
            print("\n ",joueur2.name," à un score de : ",joueur2.score.score_tic_tac_toe," point(s)")
            print("\n \n \n")
        else:
            print("\n ",joueur2.name," à un score de : ",joueur2.score.score_tic_tac_toe," point(s)")
            print("\n ",joueur1.name," à un score de : ",joueur1.score.score_tic_tac_toe," point(s)")
            print("\n \n \n")
        sortirAffichageScoreMorpion = input(" Entrez n'importe quoi pour quitter le jeu : ")
        finAffichageMorpion = True