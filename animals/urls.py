from django.urls import path
from animals.views import PetView
    # CaretakerView, VeterinarianView
app_name = 'animals'


urlpatterns = [
    path('', PetView.as_view(), name='pet'),
    # path('', CaretakerView.as_view(), name='caretaker'),
    # path('', VeterinarianView.as_view(), name='veterinarian'),
]
