class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants
    
    def augmenter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.augmenter_population()


Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)

print("Nombre d'habitants à Paris : ", Paris.get_nombre_habitants())
print("Nombre d'habitants à Marseille : ", Marseille.get_nombre_habitants())

John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloe = Personne("Chloé", 18, Marseille)

John.ajouterPopulation()
Myrtille.ajouterPopulation()
Chloe.ajouterPopulation()

print("Nombre d'habitants à Paris après l'ajout de personnes :", Paris.get_nombre_habitants())
print("Nombre d'habitant à Marseille après l'ajout de personnes : ", Marseille.get_nombre_habitants())
