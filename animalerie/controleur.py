from .models import Animal, Equipement

def cherche_occupant(lieu):
    animaux = Animal.objects.all()
    occupants = []
    for animal in animaux:
        if animal.lieu.id_equipement == lieu:
            occupants.append(animal.id_animal)
    return occupants

def nourrir(id_animal):
    animal = Animal.objects.get(id_animal=id_animal)
    mangeoire = Equipement.objects.get(id_equipement = 'mangeoire')
    if mangeoire.disponibilite == "occupe":
        animal_mang = cherche_occupant("mangeoire")
        Str_animal_mang = " ".join(animal_mang)
        return 'warning', "Impossible, la mangeoire est actuellement occupée par " + Str_animal_mang
    if animal.etat != "affame":
        return 'warning', "Désolé " + id_animal + "n'a pas faim!"
    if (animal.etat == "affame") and (mangeoire.disponibilite == "libre"):
        animal.change_lieu("mangeoire")
        animal.change_etat("repus")
        animal.save()
        return 'success', 'Félicitations, '+ id_animal+' a rejoint la mangeoire et est maintenant repus.'

def divertir(id_animal):
    animal = Animal.objects.get(id_animal=id_animal)
    roue = Equipement.objects.get(id_equipement='roue')
    if roue.disponibilite == "occupe":
        animal_roue = cherche_occupant("roue")
        Str_animal_roue = " ".join(animal_roue)
        return 'warning', "Impossible, la roue est actuellement occupée par " + Str_animal_roue
    if animal.etat != "repus":
        return 'warning',  "Désolé " + id_animal + " n'est pas en état de faire du sport!"
    if (animal.etat == "repus") and (roue.disponibilite == "libre"):
        animal.change_lieu("roue")
        animal.change_etat("fatigue")
        animal.save()
        return 'success', 'Félicitations, ' + id_animal + ' a rejoint la roue et est maintenant fatigue.'

def coucher(id_animal):
    animal = Animal.objects.get(id_animal=id_animal)
    nid = Equipement.objects.get(id_equipement='nid')
    if nid.disponibilite == "occupe":
        animal_nid = cherche_occupant("nid")
        Str_animal_nid = " ".join(animal_nid)
        return 'warning', "Impossible, le nid est actuellement occupée par " + Str_animal_nid
    if animal.etat != "fatigue":
        return 'warning', "Désolé " + id_animal + "n'est pas fatigué!"
    if (animal.etat == "fatigue") and (nid.disponibilite == "libre"):
        animal.change_lieu("nid")
        animal.change_etat("endormi")
        animal.save()
        return 'success', 'Félicitations, ' + id_animal + ' a rejoint le nid et est maintenant endormi.'

def reveiller(id_animal):
    animal = Animal.objects.get(id_animal=id_animal)
    if animal.etat != "endormi":
        return 'warning', "Désolé " + id_animal + " ne dort pas ou est déja à la litière"
    if animal.etat == "endormi":
        animal.change_lieu("litiere")
        animal.change_etat("affame")
        animal.save()
        return 'success', 'Félicitations, ' + id_animal + ' a rejoint la litière et est maintenant affamé.'