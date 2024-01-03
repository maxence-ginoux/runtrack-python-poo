class Animal:
    def __init__(self, age=0):
        self.age = age
        print("l'âge de l'animal est de", self.age, "année(s)")

    def vieillir(self):
        self.age += 1
        print("l'âge de l'animal est de", self.age, "année(s)")

    def nommer(self):
        print("L'animal se nomme Luna")




age_animal = Animal()
age_animal.vieillir()
age_animal.nommer()
