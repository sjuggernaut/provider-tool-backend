# Generated by Django 3.2 on 2022-02-01 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20211222_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
                ('app_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('provider_type', models.CharField(blank=True, choices=[('PROVIDER_TYPE_DEFAULT', 'DEFAULT'), ('PROVIDER_TYPE_NUTRITIONIST', 'NUTRITIONIST'), ('PROVIDER_TYPE_OCCUPATIONAL_THERAPIST', 'OCCUPATIONAL THERAPIST'), ('PROVIDER_TYPE_PHYSICAL_THERAPIST', 'PHYSICAL THERAPIST'), ('PROVIDER_TYPE_REGISTERED_NURSE', 'REGISTERED NURSE'), ('PROVIDER_TYPE_RESPIRATORY_THERAPIST', 'RESPIRATORY THERAPIST'), ('PROVIDER_TYPE_SOCIAL_WORKER', 'SOCIAL WORKER'), ('PROVIDER_TYPE_SPEECH_LANGUAGE_THERAPIST', 'SPEECH LANGUAGE THERAPIST')], default='PROVIDER_TYPE_DEFAULT', max_length=100, null=True)),
                ('client_status', models.CharField(blank=True, choices=[('ACTIVE_CLIENT', 'Active Client'), ('DISCHARGED_CLIENT', 'Discharged Client'), ('POTENTIAL_CLIENT', 'Potential Client')], default='POTENTIAL_CLIENT', max_length=100)),
                ('user', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Application User - Auth User')),
            ],
            options={
                'verbose_name': 'Application User',
                'verbose_name_plural': 'Application Users',
            },
        ),
    ]