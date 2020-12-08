from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from account.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    phone_number = models.CharField(
        max_length=14,
        null=False,
        unique=True
    )
    date_of_birth = models.DateField()
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'nickname', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='User'
    )
    introduce = models.TextField(
        null=True,
        max_length=200
    )

    def __str__(self):
        return str(self.user)
