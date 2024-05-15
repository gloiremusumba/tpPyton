class Forme:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

class Recta(Forme):
    def aire(self):
        return self.largeur * self.hauteur
    
class Tria(Forme):
    def aire(self):
        return self.largeur * self.hauteur/2
    
rectangle = Recta(11,5)
print(f"la surface du rectangle est:{rectangle.aire()} metre carré")

triangle = Tria(3,5)
print(f"la surface du triangle est:{triangle.aire()}metre carré")     