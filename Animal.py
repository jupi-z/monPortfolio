import abc


class Animal(abc.ABC):
    nombr = 0

    # constructeur
    def __init__(self, nom_Ac: str, especeAc: str):
        self.nom_A = nom_Ac
        self.espece = especeAc
        self.nombr += 1

    def parler(self, ):
        pass


class Chien(Animal):
    def __init__(self, nom_Ac: str, especeAc: str):
        super().__init__(nom_Ac, especeAc)

    def parler(self, ):
        return "woof"


# instancier une classe

c1 = Chien("Chien policier", "Mamifer")

print(c1.nom_A)
print(c1.espece)

print(c1.parler())
