# Generated by Django 3.2.12 on 2022-03-13 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_interviews_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Interviews',
            new_name='Interview',
        ),
    ]
