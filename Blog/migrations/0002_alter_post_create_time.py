# Generated by Django 3.2.8 on 2021-12-13 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create_time'),
        ),
    ]