from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.DecimalField(
        max_digits=15, decimal_places=0,
        null=True, blank=True, verbose_name='Телефон'
    )

    class Meta:
        db_table = 'auth_user'
