from graphviz import Graph

class Arbre:
    def __init__(self, nom):
        self.nom = nom
        self.fils = []

    def ajoute_fils(self, fils):
        self.fils.append(fils)

    def hauteur (self):
        if self.fils == []:
            return 1
        return 1 + max([fils.hauteur() for fils in self.fils])

    def taille(self):
        if self.fils == []:
            return 1
        return 1 + sum([fils.taille() for fils in self.fils])

    def binaire(self):
        return (len(self.fils) == 2) and all([fils.binaire() for fils in self.fils])

    def parcours_largeur(self):
        file = [self]
        liste = []
        while file != []:
            noeud = file.pop(0)
            liste.append(noeud.nom)
            for fils in noeud.fils:
                file.append(fils)
        return liste

    def liste_aretes(self):
        liste = []
        for fils in self.fils:
            liste.append((str(self.nom), str(fils.nom)))
            liste += fils.liste_aretes()
        return liste

    def affiche(self):
        graphe = Graph()
        graphe.edges(self.liste_aretes())
        graphe.render(view=True)

    def ajoute_position(self, nom, arbre):
        file = [self]
        while file != []:
            noeud = file.pop(0)
            if noeud.nom == nom:
                noeud.ajoute_fils(arbre)
                return
            for fils in self.fils:
                file.append(fils)
        return

    def supprime(self, nom):
        pass

if __name__ == "__main__":
    arbre = Arbre("root")
    for i in range(3): arbre.ajoute_fils(Arbre(i))
    for i in range(3):
        for j in range(3):
            arbre.ajoute_position(i, Arbre(3*(i+1) + j))
    print(arbre.hauteur())
    print(arbre.taille())
    print(arbre.parcours_largeur())
    arbre.affiche()



