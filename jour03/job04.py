class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Stats de {self.nom} (#{self.numero}) - {self.position}:")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print()


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Stats des joueurs de l'équipe {self.nom}:")
        print("---------------------------------")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, action):
        if action == "but":
            joueur.marquerUnBut()
        elif action == "passe":
            joueur.effectuerUnePasseDecisive()
        elif action == "carton_jaune":
            joueur.recevoirUnCartonJaune()
        elif action == "carton_rouge":
            joueur.recevoirUnCartonRouge()


joueur1 = Joueur("Aubameyang", 9, "Attaquant")
joueur2 = Joueur("Rongier", 10, "Milieu")
joueur3 = Joueur("Marquinhos", 4, "Défenseur")

equipe1 = Equipe("de l'OM")
equipe2 = Equipe("du PSG")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur2, "carton_jaune")
equipe2.mettreAJourStatistiquesJoueur(joueur3, "passe")

print("---------------------------------")
print("-----Stats après mise à jour-----")
print("---------------------------------")

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()