# Generated by Django 4.0.1 on 2022-01-30 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlayApp', '0003_remove_publicacion_fecha_remove_publicacion_id_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='fecha_publi',
            new_name='fecha',
        ),
    ]