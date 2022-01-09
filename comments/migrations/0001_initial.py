# Generated by Django 3.2.8 on 2021-12-20 11:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0002_alter_post_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('url', models.URLField(blank=True, verbose_name='Web-site')),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_time')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.post')),
            ],
        ),
    ]
