class CompteBancaire :
    def __init__(self, numero_de_compte, nom, prenom, solde, decouvert):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        decouvert = True

    def afficher(self):
        print("INFORMATIONS DU COMPTE")
        print("Numéro de compte :", self.__numero_de_compte)
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Découvert autorisé :") 
        if self.__decouvert is True : 
            print("Oui")
        else : 
            print("Non")
        print("Solde :", self.__solde, "€")
        print("--------------------------")

    def afficherSolde(self):
        return self.__solde
    
    def versement(self, montant_versement):
        self.__solde += montant_versement
        self.afficherSolde()

    def retrait(self, montant_retrait):
        self.__solde -= montant_retrait 
        if self.__solde < montant_retrait and self.__decouvert == False :
            print("Retrait impossible, le solde de votre compte est trop bas pour effectuer cette action.")
        self.afficherSolde()
    
    def agios(self):
        if self.__solde < 0:
            self.__solde -= 20  
            print(f"Des agios d'un montant de 20€ ont été appliqués car votre compte est à découvert.")
        self.afficherSolde()

    def virement(self, compte_receveur, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_receveur.versement(montant)
            print("Virement de", montant, "€ effectuer vers le compte", self.__numero_de_compte, "appartenant à", self.__nom, self.__prenom)
        else:
            print("Solde insuffisant. Opération de virement annulée.")
        print("--------------------------")

compte1 = CompteBancaire("1112131415161718", "Ginoux", "Maxence", 3000, False)
compte1.afficher()


compte2 = CompteBancaire("1817161514131211", "Joucaviel", "Margaux", -1000, True)
compte2.afficher()


compte1.virement(compte2, 2020)
compte1.afficher()
compte2.afficher()

