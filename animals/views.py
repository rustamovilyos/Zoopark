from django.shortcuts import render
from django.views.generic import ListView
from .models import Pet, Caretaker, Veterinarian


class PetView(ListView):
    model = Pet
    template_name = "animals/index.html"


# class CaretakerView(ListView):
#     model = Caretaker
#     template_name = "animals/index.html"


# class VeterinarianView(ListView):
#     model = Veterinarian
#     template_name = "animals/index.html"
