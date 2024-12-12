from rest_framework import viewsets
from .serializers import HeartMedicalHistorySerializer, HospitalDiseaseSerializer
from heart_app.models import Heart_Medical_History, HospitalDisease


class HeartMedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = Heart_Medical_History.objects.all()
    serializer_class = HeartMedicalHistorySerializer


class HospitalDiseaseViewSet(viewsets.ModelViewSet):
    queryset = HospitalDisease.objects.all()
    serializer_class = HospitalDiseaseSerializer
