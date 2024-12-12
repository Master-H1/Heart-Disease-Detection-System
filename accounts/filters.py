import django_filters
from heart_app.models import Patients


class PatientsFilter(django_filters.FilterSet):
    class Meta:
        model = Patients
        fields = {
            'id': ['exact', ],
            'first_name': ['icontains', ],
            'last_name': ['icontains', ]
        }
