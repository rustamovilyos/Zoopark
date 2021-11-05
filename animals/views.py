from django.shortcuts import render
from django.views.generic import ListView
from .models import Pet, Caretaker, Veterinarian


class PetView(ListView):
    model = Pet
    template_name = "animals/index.html"
    context_object_name = "pet"


class CaretakerView(ListView):
    model = Caretaker
    template_name = "animals/index.html"
    context_object_name = "care"


class VeterinarianView(ListView):
    model = Veterinarian
    template_name = "animals/index.html"
    context_object_name = "vet"
