from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddForm
from .forms import MoveForm
from django.http import HttpResponse
from .models import Animal, Equipement
import animalerie.controleur as ct


def animal_list(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()
    context = {'equipements': equipements, 'animaux': animaux}
    return render(request, 'animalerie/animal_list.html', context)

def regle(request):
    return render(request, 'animalerie/regle.html')

def add_animal(request):
    form = AddForm
    return render(request, 'animalerie/add_animal.html', {'form': form})

def equipement_detail(request, id_equipement):
    equipement = Equipement.objects.get(id_equipement=id_equipement)
    occupants_id_animal = ct.cherche_occupant(id_equipement)
    occupants = [Animal.objects.get(id_animal=id_animal) for id_animal in occupants_id_animal ]
    context = {'equipement': equipement, 'occupants': occupants}
    return render(request, 'animalerie/equipement_detail.html', context)


def animal_detail(request, id_animal):
    animal = Animal.objects.get(id_animal=id_animal)
    message, flag = '', ''
    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
        if form.is_valid():
            form.save(commit=False)
            id_nouveau_lieu = form.cleaned_data.get('lieu').id_equipement
            if id_nouveau_lieu == 'nid':
                flag, message = ct.coucher(animal.id_animal)
            if id_nouveau_lieu == 'litiere':
                flag, message = ct.reveiller(animal.id_animal)
            if id_nouveau_lieu == 'roue':
                flag, message = ct.divertir(animal.id_animal)
            if id_nouveau_lieu == 'mangeoire':
                flag, message = ct.nourrir(animal.id_animal)
            form = MoveForm()
            #flag, message = 'success', id_nouveau_lieu
            return render(request,
                          'animalerie/animal_detail.html',
                          {'animal': animal, 'form': form, 'message': message, 'flag': flag})

    else:
        form = MoveForm()
    return render(request,
                  'animalerie/animal_detail.html',
                  {'animal': animal, 'form': form, 'message': message, 'flag': flag})

