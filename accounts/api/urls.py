from rest_framework.routers import DefaultRouter
from .views import HeartMedicalHistoryViewSet, HospitalDiseaseViewSet

heartmedical_router = DefaultRouter()
hospitaldisease_router = DefaultRouter()

heartmedical_router.register(
    r'heart-medical-history', HeartMedicalHistoryViewSet)

hospitaldisease_router.register(r'hospital-disease', HospitalDiseaseViewSet)
