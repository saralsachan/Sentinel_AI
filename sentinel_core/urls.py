from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This routes any URL starting with /api/ to the api/urls.py file
    path('api/', include('api.urls')), 
]