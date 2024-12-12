from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts.api.urls import heartmedical_router, hospitaldisease_router

router = DefaultRouter()

# app1
# app2
# accounts
router.registry.extend(heartmedical_router.registry)
router.registry.extend(hospitaldisease_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
