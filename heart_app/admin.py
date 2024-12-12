from django.contrib import admin
from .models import Patients, Specialization, Doctor, Heart_Medical_History, Assigned_Test_from_Doctor_dep, RecordsFromConsult, HospitalDisease
# Register your models here.

admin.site.register(Patients)

# Doctors
admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Heart_Medical_History)
admin.site.register(Assigned_Test_from_Doctor_dep)
admin.site.register(RecordsFromConsult)
admin.site.register(HospitalDisease)
