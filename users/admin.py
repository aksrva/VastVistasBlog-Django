from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'phone_number', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'username', 'phone_number', 'is_active', 'first_name',
                'last_name', 'image'
            )
        }),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                    'user_permissions')}),
        ('Group Permissions', {'fields': ('groups', )}),
    )


admin.site.register(User, CustomUserAdmin)
