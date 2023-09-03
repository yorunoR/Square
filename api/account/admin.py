from django.contrib import admin

from .models import AdminUser, User


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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "name",
        "role",
        "activated",
        "anonymous",
        "deleted_at",
    ]

    fields = [
        "email",
        "name",
        "uid",
        "role",
        "profile_image",
        "activated",
        "anonymous",
        "created_at",
        "updated_at",
        "deleted_at",
    ]

    readonly_fields = [
        "uid",
        "anonymous",
        "created_at",
        "updated_at",
        "deleted_at",
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return User.with_deleted.all()
