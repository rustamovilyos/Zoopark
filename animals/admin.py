from django.contrib import admin
from animals.models import Caretaker, Veterinarian, Pet


# class CaretakerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'date_of_birth', 'phone_num', 'matiral_status')
# class VeterinarianAdmin(admin.ModelAdmin):
#     list_display =

admin.site.register(Caretaker)
admin.site.register(Veterinarian)
admin.site.register(Pet)
