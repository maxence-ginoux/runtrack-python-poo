class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

mon_rectangle = Rectangle(longueur=10, largeur=5)

print("Longueur de base :", mon_rectangle.get_longueur())
print("Largeur de base :", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(20)
mon_rectangle.set_largeur(10)

print("Longueur après modification :", mon_rectangle.get_longueur())
print("Largeur après modification :", mon_rectangle.get_largeur())