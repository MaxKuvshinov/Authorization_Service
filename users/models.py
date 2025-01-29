from django.db import models
from django.contrib.auth.models import AbstractUser

from users.services import generate_invite_code


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Номер телефона", help_text="Укажите номер телефона")
    invite_code = models.CharField(max_length=6, unique=True, default=generate_invite_code, verbose_name="Инвайт-код")
    referral_code = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пригласительный инвайт код")

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.phone_number
