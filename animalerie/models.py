from django.db import models


class Equipement(models.Model):
    id_equipement = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/id_equipement')

    def __str__(self):
        return self.id_equipement

    def change_disponibilite(self, dispo):
        self.disponibilite = dispo

class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def change_lieu(self, nouveau_lieu):
        ancien_lieu = self.lieu
        nouveau_lieu = Equipement.objects.get(id_equipement=nouveau_lieu)
        ancien_lieu.change_disponibilite('libre')
        ancien_lieu.save()
        if nouveau_lieu.id_equipement != 'litiere':
            nouveau_lieu.change_disponibilite('occupe')
            nouveau_lieu.save()
        self.lieu = nouveau_lieu

    def change_etat(self,nouvel_etat):
        self.etat = nouvel_etat

    def __str__(self):
        return self.id_animal
