from django.contrib import admin

from .models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "last_name",
        "first_name",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    ]

    fields = [
        "email",
        "username",
        "last_name",
        "first_name",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    ]

    readonly_fields = [
        "date_joined",
        "last_login",
    ]

    def has_add_permission(self, request, obj=None):
        return False
