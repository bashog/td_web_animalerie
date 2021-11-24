import pandas as pd
import models

data_animaux = pd.read_json('data/animaux_save.json')
data_equipements = pd.read_json('data/equipements_save.json')

# Transfert des données Animal
for a in data_animaux.columns:
    models.Animal.objects.create(id_animal=a,
                          race=data_animaux.loc["RACE", a],
                          type=data_animaux.loc["TYPE", a],
                          etat=data_animaux.loc["ETAT", a],
                          lieu=data_animaux.loc["LIEU", a]
                          )

# Transfert des données Equipement
for e in data_equipements.columns:
    models.Equipement.objects.create(id_equipement=e,
                              disponibilite=data_equipements.loc["DISPONIBILITE", e]
                             )


print("Database set")

Animal.objects.create(id_animal=a,
                          race=data_animaux.loc["RACE", a],
                          type=data_animaux.loc["TYPE", a],
                          etat=data_animaux.loc["ETAT", a],
                          lieu=data_animaux.loc["LIEU", a]
                          )