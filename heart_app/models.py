# from datetime import date
from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import GENDER_CHOICES, ChestPainType_CHOICES, RestingECG_CHOICES, ExerciseAngina_CHOICES, ST_Slope_CHOICES
# Create your models here.

# List of all diseases


class HospitalDisease(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Patients Model


class Patients(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, help_text="Please use this format: <em>YYYY-MM-DD</em>")
    sex = models.CharField(choices=GENDER_CHOICES, max_length=1)
    district = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    village = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    disease = models.ForeignKey(
        HospitalDisease, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Patients'


# Doctors Part==========================
class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Specializations'


# List of all doctors
class Doctor(models.Model):
    TITLE = (
        ('Dr.', 'Dr.'),
        ('Nurse', 'Nurse')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=1)
    photo = models.ImageField(
        upload_to="Doctors_profile", blank=True, null=True)
    title = models.CharField(choices=TITLE, max_length=100)
    specialization = models.ForeignKey(
        Specialization, on_delete=models.SET_NULL, null=True)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.first_name} - id:{self.id}'

    class Meta:
        verbose_name_plural = 'Doctors'
# ========== Doctor part end========================


# HEART Medical History
class Heart_Medical_History(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True)
    chestpaintype = models.CharField(
        choices=ChestPainType_CHOICES, max_length=50)

    restingbp = models.PositiveSmallIntegerField()
    cholesterol = models.PositiveSmallIntegerField()
    fastingbs = models.CharField(
        choices=[('0', 'less than 120 mg/dl'), ('1', 'greater than 120 mg/dl')], max_length=100)

    restingecg = models.CharField(choices=RestingECG_CHOICES, max_length=50)
    maxhr = models.PositiveIntegerField(
        validators=[MinValueValidator(60), MaxValueValidator(202)], help_text="Number between 60 and 202")

    exerciseangina = models.CharField(
        choices=ExerciseAngina_CHOICES, max_length=50)
    oldpeak = models.FloatField()
    st_slope = models.CharField(choices=ST_Slope_CHOICES, max_length=20)
    date_recorded = models.DateField(auto_now_add=True)
    heartdisease = models.PositiveBigIntegerField(
        choices=[(0, 0), (1, 1)], blank=True, null=True)

    def __str__(self):
        return f'{self.patient.first_name}'

    # Calculate patient ages
    def get_age(self):
        today_year = int(date.today().strftime('%Y'))
        year_of_birth = int(self.patient.date_of_birth.strftime('%Y'))
        age = today_year - year_of_birth
        return int(age)

    # Save age and sex of patient
    def save(self, *args, **kwargs):
        self.sex = self.patient.sex
        self.age = self.get_age()
        super().save()

    class Meta:
        verbose_name_plural = 'Medical History'
# ====== Heart medical history end======================


# This is data that will be sent by Doctor to Laboratorian
class Assigned_Test_from_Doctor_dep(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.id} -- {self.patient.first_name}'


# These are data from consultation department
class RecordsFromConsult(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient.id} -- {self.patient.first_name}'
