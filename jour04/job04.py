class Forme:
    def aire():
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        print("L'aire de ce rectangle est de", self.largeur * self.hauteur, "cm².") 
        

rectangle1 = Rectangle(5, 4)
rectangle1.aire()