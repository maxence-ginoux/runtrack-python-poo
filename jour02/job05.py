class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir


    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer. Le niveau d'essence dans le réservoir est trop bas.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    def __verifier_plein(self):
        return self.__reservoir > 5


ma_voiture = Voiture(marque="BMW", modele="M3 Touring", annee=2023, kilometrage=15000)

print(f"Marque: {ma_voiture.get_marque()}")
print(f"Modèle: {ma_voiture.get_modele()}")
print(f"Année: {ma_voiture.get_annee()}")
print(f"Kilométrage: {ma_voiture.get_kilometrage()} km")
print(f"En marche: {ma_voiture.get_en_marche()}")
print(f"Réservoir: {ma_voiture.get_reservoir()} litres")

ma_voiture.demarrer()
ma_voiture.arreter()