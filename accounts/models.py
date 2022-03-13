from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT

from .managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class SensitiveUserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT)
    resident_registration_number = models.CharField(max_length=30, unique=True, verbose_name="주민등록번호 13자리")
    bank_account_number = models.CharField(max_length=31, unique=True, verbose_name="계좌번호")