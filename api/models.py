from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

#Custom User (role based RBAC)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('operator', 'Operator'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
#cAMERA nODE
class CameraNode(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Camera @ {self.location}"
    
#Incident ()Notice the foreign key
class Incident(models.Model):
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    camera = models.ForeignKey(CameraNode, on_delete=models.CASCADE, related_name='incidents')
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='low')
    detection_class = models.CharField(max_length=100) #E.G. PERSON AFTER HOURS
    ai_assessment = models.TextField(blank=True, null=True) #POPULATED BY LANGRAPH
    
    def __str__(self):
        return f"{self.severity.upper()} Incident at {self.camera.location}"

