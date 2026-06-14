from rest_framework import serializers
from .models import CameraNode, Incident

class CameraNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraNode
        #explicitly list the fields we want to expose to the frontend
        fields = ['id', 'location', 'is_active', 'registered_at']

class IncidentSerializer(serializers.ModelSerializer):
    # This ensures the camera's location string is sent along with the incident,
    # rather than just the UUID, saving the frontend an extra API call.
    camera_location = serializers.ReadOnlyField(source='camera.location')

    class Meta:
        model = Incident
        fields = ['id', 'camera', 'camera_location', 'timestamp', 'severity', 'detection_class', 'ai_assessment']