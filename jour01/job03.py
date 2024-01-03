class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        print("le nombre1 est", nombre1)
        print("le nombre2 est", nombre2)
    
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("l'addition des deux est égales à", resultat)

test = Operation(12, 3)
test.addition()