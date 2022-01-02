# Generated by Django 3.2 on 2021-12-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casemanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemanagerusers',
            name='provider_type',
            field=models.CharField(blank=True, choices=[('PROVIDER_TYPE_DEFAULT', 'DEFAULT'), ('PROVIDER_TYPE_NUTRITIONIST', 'NUTRITIONIST'), ('PROVIDER_TYPE_OCCUPATIONAL_THERAPIST', 'OCCUPATIONAL THERAPIST'), ('PROVIDER_TYPE_PHYSICAL_THERAPIST', 'PHYSICAL THERAPIST'), ('PROVIDER_TYPE_REGISTERED_NURSE', 'REGISTERED NURSE'), ('PROVIDER_TYPE_RESPIRATORY_THERAPIST', 'RESPIRATORY THERAPIST'), ('PROVIDER_TYPE_SOCIAL_WORKER', 'SOCIAL WORKER'), ('PROVIDER_TYPE_SPEECH_LANGUAGE_THERAPIST', 'SPEECH LANGUAGE THERAPIST')], default='PROVIDER_TYPE_DEFAULT', max_length=100, null=True),
        ),
    ]
