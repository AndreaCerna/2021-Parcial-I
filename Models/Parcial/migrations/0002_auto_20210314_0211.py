# Generated by Django 3.1.7 on 2021-03-14 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parcial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='nombre_categoria',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='nombre_categoria',
        ),
    ]