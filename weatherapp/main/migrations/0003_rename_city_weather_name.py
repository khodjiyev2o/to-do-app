# Generated by Django 4.0.2 on 2022-02-11 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_person_weather'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='city',
            new_name='name',
        ),
    ]
