class Somme:
    def __init__(self,note1,note2):
        self.note1=note1
        self.note2=note2
    def som(self,note1,note2):
        result=note1 + note2
        return result

nbr1 = int(input("Entrer nombre 1 :"))
nbr2 = int(input("Entrer nombre 2 :"))

som_a= Somme(nbr1 , nbr2)

print(f"La somme de ces deux nombres saisie est de {som_a.som(nbr1,nbr2)}")