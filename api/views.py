from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CameraNode, Incident
from .serializers import CameraNodeSerializer, IncidentSerializer

class CameraNodeViewSet(viewsets.ModelViewSet):
    queryset = CameraNode.objects.all()
    serializer_class = CameraNodeSerializer
    # This locks the endpoint. No valid JWT = 401 Unauthorized.
    permission_classes = [IsAuthenticated]

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by('-timestamp') # Newest first
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]