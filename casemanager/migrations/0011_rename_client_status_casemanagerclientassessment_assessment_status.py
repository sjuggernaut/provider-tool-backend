# Generated by Django 3.2 on 2021-12-09 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casemanager', '0010_alter_casemanagerclientassessment_client_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casemanagerclientassessment',
            old_name='client_status',
            new_name='assessment_status',
        ),
    ]