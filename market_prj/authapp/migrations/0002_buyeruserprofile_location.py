# Generated by Django 5.1.5 on 2025-02-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyeruserprofile',
            name='location',
            field=models.CharField(blank=True, max_length=128, verbose_name='Адрес'),
        ),
    ]
