import numpy as np
from Voiture import Voiture

class Agence:
    def __init__(self, nom_agence="", adresse_agence="", liste_voitures=[]):
        self.nom_agence = nom_agence
        self.adresse_agence = adresse_agence
        self.liste_voitures = liste_voitures

    # fonction affiche agence      
    def afficher_agence(self):
        print("Nom Agence : ", self.nom_agence)
        print("Adresse Agence : ", self.adresse_agence)
        print("Liste des voitures: ")
        for voiture in self.liste_voitures:
            voiture.affiche()

    def add_voiture(self, voiture):
        self.voitures.append(voiture)

    def delete_voiture(self, voiture):
        self.voitures.remove(voiture)
    
            
     # fonction rechercher voiture
    def rechercher_voiture(self, matricule):
        for voiture in self.liste_voitures:
            if voiture.matricule == matricule:
                print("la voiture existe !!")
                return voiture
        return None
    
                
    def tri_voiture_selon_date(self):
        self.voitures.sort(key=lambda x: x.dat_circ)
        self.show_voitures()
    
    def get_voiture_plus_recente_selon_date(self):
        self.tri_voiture_selon_date()
        return self.voitures[0]
    
    def get_voiture_plus_anciennne_selon_date(self):
        self.tri_voiture_selon_date()
        return self.voitures[-1]
    
    

