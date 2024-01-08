class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True 

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():  
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():  
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté, donc il ne peut pas être rendu.")

mon_livre = Livre(titre="Harry Potter", auteur="J.K. Rowling", nb_pages=300)

print("Disponibilité initiale :", mon_livre.verification())

mon_livre.emprunter()
mon_livre.emprunter()
mon_livre.rendre()
mon_livre.rendre()