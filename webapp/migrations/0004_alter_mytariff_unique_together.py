# Generated by Django 4.0.4 on 2022-05-18 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_mytariff_tariff_alter_mytariff_user_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mytariff',
            unique_together=set(),
        ),
    ]
