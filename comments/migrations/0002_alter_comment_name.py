# Generated by Django 3.2.8 on 2022-02-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=70, verbose_name='name'),
        ),
    ]
