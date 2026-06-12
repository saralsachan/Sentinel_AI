from django.contrib import admin
from .models import CameraNode, Incident, User
from django.contrib.auth.admin import UserAdmin

#the UserAdmin interface has predefined fiels to show, so it does not give us option to select role that we defined in out User
class CustomAdminUser(UserAdmin):
    # 1. Add 'role' to the screen when editing an existing user
    fieldsets = UserAdmin.fieldsets + (
        ('Sentinel RBAC', {'fields': ('role',)}),
    )
    # 2. Add 'role' to the screen when creating a brand new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Sentinel RBAC', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff')
    

admin.site.register(CameraNode)
admin.site.register(Incident)
admin.site.register(User, CustomAdminUser) #using django's built in user admin interface,
