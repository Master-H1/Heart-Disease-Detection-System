from rest_framework import serializers
from heart_app.models import Heart_Medical_History, HospitalDisease


class HeartMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Heart_Medical_History
        fields = '__all__'


class HospitalDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalDisease
        fields = '__all__'
