from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, max_length=150)

    objects = AdminUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = "admin_users"
        verbose_name = "管理者"
        verbose_name_plural = "管理者"


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        query = super().get_queryset()

        query = query.filter(deleted_at=None)

        return query


class BasicModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeleteManager()
    with_deleted = models.Manager()

    class Meta:
        abstract = True


class User(BasicModel):
    activated = models.BooleanField(default=False)
    email = models.EmailField()
    name = models.CharField(max_length=150)
    profile_image = models.CharField(blank=True, null=True)
    role = models.IntegerField(default=0)
    uid = models.CharField(max_length=150)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"
        indexes = [
            models.Index(fields=["email"], condition=models.Q(email__isnull=False), name="index_users_on_email"),
            models.Index(fields=["uid"], condition=models.Q(uid__isnull=False), name="index_users_on_uid"),
        ]
