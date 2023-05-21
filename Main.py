from Voiture import Voiture
from Agence import Agence
from datetime import date
 
if __name__=='__main__' :
    v1 = Voiture("246 TN 3000", "Kia", date(2001, 5, 5), 60000, 1700, "gris", 170)
    v2 = Voiture("183 TN 2588", "Jeep", date(2012, 11, 11), 50000, 1600, "blanc", 160)
    v3 = Voiture("233 TN 2547", "Ford", date(2010, 5, 5), 60000, 1700, "gris", 150)
    v1.saisie()
    v1.affiche()