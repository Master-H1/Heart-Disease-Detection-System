from django import forms
from .models import UserRoleManager
from heart_app.models import Patients, Heart_Medical_History


# Additional data to User accounts form
class UserRoleManagerForm(forms.ModelForm):
    class Meta:
        model = UserRoleManager
        fields = ('role',)


# Form for Adding patient records
class PatientsForm(forms.ModelForm):

    date_of_birth = forms.DateInput(format='YYYY-MM-DD')

    class Meta:
        model = Patients
        fields = '__all__'

        widgets = {
            'sex': forms.Select(attrs={'style': "width:170px; height:50px;margin-top:30px; margin-right:2px;"}),
        }


# Heart Medical History form
class HeartMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = Heart_Medical_History
        fields = ['chestpaintype', 'restingbp', 'cholesterol', 'fastingbs', 'restingecg', 'maxhr', 'exerciseangina',
                  'oldpeak', 'st_slope',]
