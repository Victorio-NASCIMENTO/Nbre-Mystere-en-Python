from random import randint


print("\nBienvenue dans le jeu \033[93mNombre Mystère\033[0m de Victorio.\nChoisissez le niveau de difficulté.\n")
niveaux = ["Nombre entre 0 et 10.",
           "Nombre en 0 et 100.",
           "Nombre entre 0 et 1000.",
           "Nombre entre 0 et 10_000.",
           "Nombre entre 0 et 100_000."
]

for i in range(len(niveaux)) : print(f"\033[32m{i + 1}-\033[0m {niveaux[i]}\n")

while 1 :
    choix = input("Votre choix : ")
    if(choix.isdigit() == 1 and 1 <= int(choix) <= 5) :
        choix = int(choix)
        break
    else : print("\n\033[91m!!!\033[0mVeuillez entre un entier entre 1 et 5.\n")

max = 10**choix
Nbre_Mystere = randint(0, max)
Nbre_Essais = 0
while 1 : 
    choix = input(f"\n\033[93mDevinez le nombre mystère dans [0,{max}]: \033[0m")
    if(choix.isdigit() == 0) : print("\n\033[91m!!!\033[0mVeuillez entrer un entier positif")
    else :
        Nbre_Essais += 1
        choix = int(choix)
        if(choix < Nbre_Mystere) : print("\nTrop petit.")
        elif(choix > Nbre_Mystere) : print("\nTrop grand")
        else : 
            print(f"\nFélicitations. Vous avez trouvé le \033[40mnombre mystère en {Nbre_Essais} coup(s).\033[0m")
            print(f"\n\033[32mNote : {int((max - Nbre_Essais)*20/max)}.\033[0m\nBye.\n")
            break
input("\nAppuyez Entrée pour fermer le programme :) : ")
