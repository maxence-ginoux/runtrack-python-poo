class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello !")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
        print("En faite j'ai menti j'ai", self.age, "ans ...")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

    def afficherAge(self):
        print("J'ai", self.age, "ans.")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age):
        self.__matiereEnseignee = matiereEnseignee
        self.age = age
    def enseigner(self):
        print("Le cours va commencer !")

# créations des instances      
Max = Personne()
Soso = Eleve()
Luc = Professeur("cybersécurité", 40)

#appelle des méthodes
Soso.bonjour()
Soso.afficherAge()
Soso.allerEnCours()
Soso.modifierAge(15)
print("---------------------------")
Luc.bonjour()
Luc.enseigner()