class Account:
        def __init__(self,solde_initual=0):
            self.solde_initual=solde_initual
            self.solde_actuel= self.solde_initual
        
        def getBalance(self):
            return self.solde_actuel
        
        def deposer(self,montant):
            self.solde_actuel=self.solde_actuel + montant
        
        def retirer(self,montant):
            self.solde_actuel=self.solde_actuel - montant
        
        def ajouter_Interet(self,taux):
            self.solde_actuel= self.solde_actuel *(1 + taux)


Depot=int(input("entrer un montant à deposer:"))
Retraint=int(input("entrer le montant à retirer:"))

compte=Account()
compte.deposer(Depot)
compte.retirer(Retraint)

compte.ajouter_Interet(int(input("enter le taux du jour :")))

print(compte.getBalance())

