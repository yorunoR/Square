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
