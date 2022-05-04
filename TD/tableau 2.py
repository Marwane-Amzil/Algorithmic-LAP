from numpy import *
import random as rd
import time

def tableau_initial(taille):
    tab = zeros(taille, dtype=int)
    return tab


def remplissage(tab,n:int):
    for i in range (taille):
        rdm=rd.randint(0,n)
        tab[i]=rdm
    return tab


def rech_val_min(tab):
    for j in range (0,len(tab)):
        if tab[j]==min(tab):
            a = tab[j]
    return a
def occurence(tab,lui:int):
    a = 0
    for i in range (0,len(tab)):
        if tab[i] == lui:
            a=a+1
        else:
            print('ce nombre n est pas dans le tableau')
    return a

def recherche(tab,rechercher,):
    for i in range (0,len(tab)):
        if tab[i]==rechercher:
            return rechercher,'existe'
    return rechercher,'n existe pas'

def moyenne(tableau):
    moy = 0
    for i in range (0,10):
        a = tableau[i]
        moy = moy + a
    moy = moy / 10
    return moy

def eclatement(tab,):
    precedent=tab[1]
    rangerdansV1=True
    n1=0
    n2=0
    for i in range (0,len(tab)):
        if tab[i] < precedent:
            rangerdansV1=False
        elif rangerdansV1:
            n1=n1+1
            tab[n1]=tab[i]
        else:
            n2=n2+1
            tab[n2]=tab[i]
        precedent=tab[i]
taille = 10
tab=tableau_initial(taille)
print(eclatement(tab))



if __name__ == "__main__":
    taille=int(input("choisir la taille: "))
    tab = tableau_initial(taille)
    val_max = int(input("choisissez la valeur max"))
    fini=False
    while not fini:
        print(' [1] -> Remplir aléatoirement un tableau ')
        print(' [2] -> Afficher un tableau ')
        print(' [3] -> Rechercher la valeur minimum d’un tableau ')
        print(' [4] -> Compter le nombre d’occurrences d’une valeur demandée à l’utilisateur dans un tableau ')
        print(' [5] -> Rechercher une valeur dans un tableau ')
        print(' [6] -> Calculer la moyenne des valeurs d’un tableau ')
        print(' [7] -> Quitter ')
        choix = int(input("quel est votre chois : "))
        if choix == 1:
            tab = remplissage(tab,val_max)
        elif choix == 2 :
            print(tab)
        elif choix == 3:
            print('le chiffre le plus petit est = ', rech_val_min(tab))
        elif choix == 4:
            lui=int(input('quel chiffre voulez vous '))
            print('il y a', occurence(tab,lui),lui,'dans le tableau')
        elif choix == 5:
            rechercht=int(input('quel nombre voulez savoir s il existe dans le tableau'))
            print(recherche(tab,rechercht))
        elif a==6:
                print('La moyenne est de : ', str(moyenne(tab)))
    time.sleep(1)
