class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            print(f"{nombre_credits} crédits ajoutés !")
          
            self.__level = self.__studentEval()
        else:
            print("Erreur ! Le nombre de crédits ajoutés doit être supérieur à zéro !")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

  
    def studentInfo(self):
        print("\nInformations de l'étudiant:")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Identifiant: {self.__numero_etudiant}")
        print(f"Niveau: {self.__level}")
        print(f"Total de crédits: {self.__credits} crédits.")


john_doe = Student(nom="Doe", prenom="John", numero_etudiant=145)

john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)

john_doe.studentInfo()