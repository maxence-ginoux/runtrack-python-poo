class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut : {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        tache_a_supprimer = next((tache for tache in self.taches if tache.titre == titre), None)
        if tache_a_supprimer:
            self.taches.remove(tache_a_supprimer)
            print(f"Tâche '{titre}' supprimée.")
        else:
            print(f"Tâche '{titre}' non trouvée.")

    def marquerCommeFinie(self, titre):
        tache_a_modifier = next((tache for tache in self.taches if tache.titre == titre), None)
        if tache_a_modifier:
            tache_a_modifier.statut = "Terminée"
            print(f"Tâche '{titre}' marquée comme terminée.")
        else:
            print(f"Tâche '{titre}' non trouvée.")

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


# les tâches
tache1 = Tache("faire du sport", "Allez à la salle de boxe")
tache2 = Tache("faire le plein d'essence", "Allez à la station service")
tache3 = Tache("manger sainement", "cuisiner des légumes")

# la liste des tâches
liste_taches = ListeDeTaches()

# Ajouter tâches dans liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Afficher liste
print("Liste initiale des tâches :")
liste_taches.afficherListe()

# Supprimer tache
liste_taches.supprimerTache("faire le plein d'essence")

# Marquage d'une tâche comme terminée
liste_taches.marquerCommeFinie("faire du sport")


print("\nListe mise à jour des tâches :")
liste_taches.afficherListe()

# reste à faire
taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)