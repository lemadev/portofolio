# Generated by Django 3.1.1 on 2020-09-06 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminhospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='date',
        ),
    ]