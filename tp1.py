class Etudiant:
    def __init__(self,name,note1,note2):
        self.name=name
        self.note1=note1
        self.note2=note2
    def calcul_moyenne(self):
        note=[self.note1,self.note2]
        some =sum(note)
        self.calcule_moyenne =some/2
    def affiche_nom_moyenne(self):
        afficher_name_moyenne= f"L'etudiant {self.name} a la moyenne de:{self.calcule_moyenne}" 
        return afficher_name_moyenne

name=input("Saisire le nom de l'etudiant: ")  
note1=float(input("Quel est la note1: ")) 
note2=float(input("Quel est la note2: "))  

etudiant = Etudiant(name,note1,note2)
etudiant.calcul_moyenne() 
print(etudiant.affiche_nom_moyenne())
