# Generated by Django 3.1.2 on 2020-10-11 12:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Client', '0003_score_maximum'),
        ('Course', '0002_auto_20201011_1737'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.RenameModel(
            old_name='SeminarMessages',
            new_name='SeminarMessage',
        ),
    ]