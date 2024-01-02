class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("coordonnées du point :", self.x,",", self.y)

    def afficherX(self):
        print("la position de x est:", self.x)

    def afficherY(self):
        print("la position de y est:", self.y)

    def changerX(self, nouveau_x):
        self.x = nouveau_x
        
    def changerY(self, nouveau_y):
        self.y = nouveau_y


valeurpoint = Point(10, 20)

valeurpoint.afficherLesPoints()
valeurpoint.afficherX()
valeurpoint.afficherY()

valeurpoint.changerX(15)
valeurpoint.changerY(25)
valeurpoint.afficherLesPoints()
