#importer datetime pour la date de circulation
import numpy as np
from datetime import datetime

class Voiture :
    def __init__(self, marque='', matricule='', dat_circ=datetime.now(), kilometrage='', cylindre=0,couleur='') :
        self.marque = marque 
        self.matricule = matricule
        self.dat_circ = dat_circ
        self.kilometrage = kilometrage
        self.cylindre = cylindre
        self.couleur = couleur

    def saisie(self) :
        self.marque = input("Marque :")
        self.matricule = input("matricule :")
        self.dat_circ = input("dat_circulation :")
        self.dat_circ = datetime.strptime(self.dat_circ, '%Y-%m-%d')
        self.kilometrage = input("kilometrage :")
        self.cylindre = int(input("cylindre :"))
        self.couleur = int(input("couleur :"))
    
    def affiche(self) :
        print("\n**************** Voiture ***************\n")
        print(f"Matricule: %s \nMarque: %s \nDate de circulation: %s \nKilometrage: %s \nCylindre: %s \nCouleur: %s \n" % (self.matricule, self.marque, self.date_circulation, self.kilometrage, self.cylindre, self.couleur))
    
         
    def voiture_Vector(self):
        return np.array([self.kilometrage, self.cylindre])

    # normaliser les données    
    def normaliser_les_voitures(voiture):
        vecteur = voiture.voiture_Vector()
        mean = np.mean(vecteur)
        std = np.std(vecteur) #standard deviation 
        vecteur_normalise = (vecteur - mean) / std
        return vecteur_normalise
    
   