# Generated by Django 4.0.1 on 2022-01-23 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlayApp', '0004_rename_clave_usuario_clave1_usuario_clave2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='clave2',
        ),
    ]