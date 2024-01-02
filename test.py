class Operation:
    def addition(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        print("le nombre1 est", nombre1)
        print("le nombre2 est", nombre2)
        resultat = self.nombre1 + self.nombre2
        print("l'addition des deux est égales à", resultat)

Operation(12, 3)
print(Operation.addition)