# Generated by Django 3.2 on 2021-10-05 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('reviewboard', '0002_auto_20211005_1019'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewBoardMember',
            new_name='ReviewBoardUser',
        ),
    ]
