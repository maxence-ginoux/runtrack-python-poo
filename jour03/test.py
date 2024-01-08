class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__numero_compte} - {self.__nom} {self.__prenom}")
        print(f"Solde: {self.__solde} euros")
        print(f"Peut aller à découvert: {self.__decouvert}")
        print("------------------------------")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} euros")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} euros effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__decouvert or self.__solde >= montant:
            self.__solde -= montant
            print(f"Retrait de {montant} euros effectué.")
        else:
            print("Opération impossible. Solde insuffisant.")
        self.afficherSolde()

    def agios(self):
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.05  
            print(f"Des agios de {agios} euros ont été appliqués.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} euros effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Opération impossible. Solde insuffisant.")
        self.afficherSolde()


compte1 = CompteBancaire("123456", "pain", "d'épice", 5000)
compte1.afficher()

compte2 = CompteBancaire("789012", "pain", "olé", -1000, decouvert=True)
compte2.afficher()

compte1.virement(compte2, 1000)
compte1.afficher()
compte2.afficher()