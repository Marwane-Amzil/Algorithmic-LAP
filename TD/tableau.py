import numpy as np
import random as rd
import time

def tableau_erreur():
    tableau_vide=np.zeros((10),dtype=int)
    return tableau_vide
tableau_erreur()
def recherche(tableau):
    a = tableau[1]
    for i in range (0,len(tableau)):
        if tableau[i]<min:
            a = tableau[i]
    return a

def moyenne(tableau)->np.dtype:
    moy = 0
    for i in range (0,10):
        a = tableau[i]
        moy = moy + a
    moy = moy / 10
    return moy

def occurrence(tableau, a):
    nbr = 0
    for i in range (0,10):
        if tableau[i]==a:
            nbr = nbr + 1
    return nbr

def rec(tableau, a):
    for i in tableau:
        if tableau[i]==a:
            return True
    return False

def menu():
    print(' [1] -> Remplir aléatoirement un tableau ')
    print(' [2] -> Afficher un tableau ')
    print(' [3] -> Rechercher la valeur minimum d’un tableau ')
    print(' [4] -> Compter le nombre d’occurrences d’une valeur demandée à l’utilisateur dans un tableau ')
    print(' [5] -> Rechercher une valeur dans un tableau ')
    print(' [6] -> Calculer la moyenne des valeurs d’un tableau ')
    print(' [7] -> Quitter ')
    tableau = np.empty(10,dtype=np.int_)
    tableau: np.empty
    a=2
    while 0<=a:
        a= int(input('Choississez ce que vous voulez : '))
        if a!= 7:
            if a==1:
                tableau = np.random.randint(10,size=10)
                print (tableau)
            elif a==2:
                print (tableau)
            elif a==3:
                print('Le minimum est : ' ,str(recherche(tableau)))
            elif a==4:
                valeur=int(input('De quelle valeur voulez-vous l occurrence ? ' '\n ---> '))
                print('Il y a',occurrence(tableau, valeur), '', valeur, 'dans le tableau.')
            elif a==5:
                valeur=int(input('Quelle valeur cherchez-vous ? ' '\n ---> '))
                print(rec(tableau, valeur))
            elif a==6:
                print('La moyenne est de : ', str(moyenne(tableau)))
            else :
                print ('Entrez un nombre valide.')
        else :
            print('Au revoir')
            time.sleep(1)
            a = -1

if __name__ == "__main__":
    menu()