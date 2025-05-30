# Generated by Django 5.2.1 on 2025-05-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('telefono', models.CharField(max_length=15, unique=True, verbose_name='Telefono')),
                ('fotografia', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='fotos', verbose_name='Fotografia')),
            ],
        ),
    ]
