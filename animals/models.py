from django.db import models
from django.core.validators import MaxValueValidator
gender_choice = (
    ('male', 'male'),
    ('female', 'female'),
    ('baby', 'baby'),
)

matiral_status_choice = (
    ('married', 'married'),
    ('not married', 'not married'),
    ('single', 'single')
)

ration_type_choice = (
    ('baby feeding', 'baby feeding'),
    ('diet feeding', 'diet feeding'),
    ('enhanced feeding', 'enhanced feeding'),
)


# Caretaker
# id(int),
# name(charfield),
# date_of_birth(date),
# phone_num(int),
# matiral_status(charfield),
class Caretaker(models.Model):
    gender = models.CharField(max_length=6, choices=gender_choice, null=True)
    name_is = models.CharField(max_length=25)
    date_of_birth = models.DateField(max_length=8)
    phone_num = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    matiral_status = models.CharField(max_length=15, choices=matiral_status_choice)

    def __str__(self):
        return self.name_is


# Veterinarian
# id(int),
# name(charfield),
# date_of_birth(date),
# phone_num(int),
# matiral_status(charfield)

class Veterinarian(models.Model):
    gender = models.CharField(max_length=6, choices=gender_choice, null=True)
    name = models.CharField(max_length=25)
    date_of_birth = models.DateField(max_length=8)
    phone_num = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    matiral_status = models.CharField(max_length=15, choices=matiral_status_choice)

    def __str__(self):
        return self.name


# Pet
# date_of_birth(datefield),
# gender(charfield),
# wintering{
# code(int, blank=True),
# 	country_name(charfield, blank=True),
# 	flight_date(date, blank=True),
# 	arrival_date(date, blank=True),
# 	}
# reptile{
# 	temperature(charfield, blank=True),
# 	hibernation_timing(int, blank=True),
# },
# habitat(charfield),
# about_habibat(textfield)
# ration_num(int),
# ration_name(charfield),
# ration_type(charfield),
# foreignkey::caretaker,
# foreignkey::veterinrian,
class Pet(models.Model):
    pseudonym = models.CharField(max_length=15, null=True)
    date_of_birth = models.DateField(max_length=8)
    gender = models.CharField(max_length=6, choices=gender_choice)
    code_wintering = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True)
    flight_date = models.DateField(max_length=8, null=True ,blank=True)
    arrival_date = models.DateField(max_length=8, null=True, blank=True)
    temperature = models.CharField(max_length=4, null=True, blank=True)
    hibernation_timing = models.FloatField(max_length=3, null=True, blank=True)   #сроки зимней спячки
    habibate = models.CharField(max_length=45)
    about_of_habibate = models.TextField(max_length=1000, null=True, blank=True)
    ration_num = models.IntegerField(validators=[MaxValueValidator(99999)], null=True)
    ration_name = models.CharField(max_length=30)
    ration_type = models.CharField(max_length=16, choices=ration_type_choice)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    veterinrian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)

    def __str__(self):
        return self.pseudonym
