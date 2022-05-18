from django.contrib.auth import get_user_model
from django.db import models


class MyTariff(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='tariffs', verbose_name='Абонент'
    )
    tariff = models.ForeignKey(
        'webapp.AllTariff', on_delete=models.CASCADE,
        related_name='tariffs', verbose_name='МойТариф'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата покупки'
    )


class AllTariff(models.Model):
    title = models.CharField(
        max_length=100, null=False,
        blank=False, verbose_name='Название тарифа'
    )
    min = models.DecimalField(
        max_digits=5, decimal_places=0,
        null=False, blank=False, verbose_name='Минута'
    )
    gb = models.DecimalField(
        max_digits=5, decimal_places=0,
        null=False, blank=False, verbose_name='Гигабайт'
    )
    sms = models.DecimalField(
        max_digits=5, decimal_places=0,
        null=False, blank=False, verbose_name='СМС'
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=0,
        null=False, blank=False, verbose_name='Цена'
    )


class Like(models.Model):
    tariff = models.ForeignKey(
        to='webapp.AllTariff', on_delete=models.CASCADE,
        related_name='likes', verbose_name='Тариф'
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='likes'
    )

    class Meta:
        unique_together = ['user', 'tariff']
