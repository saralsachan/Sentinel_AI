from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CameraNodeViewSet, IncidentViewSet

# The router automatically creates /incidents/ and /incidents/<id>/ routes
router = DefaultRouter()
router.register(r'cameras', CameraNodeViewSet)
router.register(r'incidents', IncidentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]