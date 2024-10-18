from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.


def pet_add_page(request):
    return render(request, 'pets/pet-add-page.html')


def pet_edit_page(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete_page(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def pet_details_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)
