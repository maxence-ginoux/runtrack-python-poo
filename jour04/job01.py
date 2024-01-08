class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        nouvel_age = int(input("Veuillez entrer le nouvel âge de la personne :"))
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours():
        print("Je vais en cours")

    def afficherAge(self):
        print("j'ai", self.age, "ans.")

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner():
        print("Le cours va commencer")
        
Max = Personne()
Soso = Eleve()

Soso.afficherAge()



