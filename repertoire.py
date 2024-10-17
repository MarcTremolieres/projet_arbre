from arbre import Arbre
import os

def genere_arbre(chemin="./"):
    os.chdir(chemin)
    chemin = os.getcwd()
    liste = os.scandir()
    nom = chemin.split(sep="/")[-1]
    print(nom)
    arbre = Arbre(nom)
    liste = os.scandir()
    for item in liste:
        print(item.name, item.is_dir())
        if item.name[0] in (".", "_"): continue
        if item.is_dir():
            acces = chemin + "/" + item.name
            arbre.ajoute_fils(genere_arbre(acces))
        else:
            arbre.ajoute_fils(Arbre(item.name))
    return arbre


chemin = os.getcwd()
'''
print()
print()'''
arbre = genere_arbre("../")
arbre.affiche()


