class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def droite(self):
        self.x += 1

    def gauche(self):
        self.x -= 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        print("position du personnage :", self.x,",", self.y)

#Utilisation acvec position initialjoueurPersonnage(0, 0)
joueur = Personnage(0, 0)

#Déplacements
joueur.gauche()
joueur.haut()

joueur.position()