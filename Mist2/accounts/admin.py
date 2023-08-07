from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


# Register your models here.

@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    pass


def create_user_groups():
    superuser_group, _ = Group.objects.get_or_create(name='Superusers')
    superuser_permissions = Permission.objects.all()  # Add all permissions to superusers
    superuser_group.permissions.set(superuser_permissions)

    staff_group, _ = Group.objects.get_or_create(name='Staff')
    staff_permissions = Permission.objects.filter(
        codename__in=['add_game', 'change_game', 'view_game'])  # Define limited permissions
    staff_group.permissions.set(staff_permissions)


# Call the function to create the user groups and assign permissions
create_user_groups()


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Add 'groups' field to User change form
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('groups',)}),
    )


# Register the custom UserAdmin
admin.site.unregister(UserModel)
admin.site.register(UserModel, UserModelAdmin)
