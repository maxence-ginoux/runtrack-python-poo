class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur


    def perimetre(self):
        valeur_perimetre = (self.__longueur + self.__largeur) * 2
        print("Le périmètre de ce rectangle est de", valeur_perimetre, "cm.")

    def surface(self):
        valeur_surface = self.__longueur * self.__largeur
        print("La surface de ce rectangle est de", valeur_surface, "cm².")

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, largeur, longueur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        valeur_volume = self.get_longueur() * self.get_largeur() * self.__hauteur
        print("Le volume de ce rectangle est de", valeur_volume, "m³.")

forme = Rectangle(10, 5)
forme.perimetre()
forme.surface()

geometrie = Parallelepipede(10, 5, 8)
geometrie.volume()