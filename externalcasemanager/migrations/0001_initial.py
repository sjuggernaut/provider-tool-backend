# Generated by Django 3.2 on 2022-02-09 22:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0007_alter_applicationuser_client_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalCMClientIntervention',
            fields=[
                ('client_assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('created_time', models.TimeField(auto_now_add=True, null=True)),
                ('assessment_status', models.CharField(blank=True, choices=[('NEW_CASE_MANAGEMENT_CLIENT', 'New Case Management Client'), ('EXISTING_CASE_MANAGEMENT_CLIENT', 'Existing Case Management Client')], db_column='assessment_status', default='NEW_CASE_MANAGEMENT_CLIENT', max_length=100)),
                ('assessment_date', models.DateField(blank=True, null=True)),
                ('internal_comm_assessment_clinical_notes', models.TextField(blank=True, null=True)),
                ('internal_comm_followup_clinical_notes', models.TextField(blank=True, null=True)),
                ('internal_comm_internal_referral_notes', models.TextField(blank=True, null=True)),
                ('external_comm_external_referral_organization', models.TextField(blank=True, null=True)),
                ('external_comm_external_followup_organization', models.TextField(blank=True, null=True)),
                ('casemanager', models.ForeignKey(db_column='casemanager', on_delete=django.db.models.deletion.PROTECT, related_name='external_intervention_casemanager', to='authentication.applicationuser', verbose_name='Case Manager')),
                ('client', models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.PROTECT, related_name='external_intervention_client', to='authentication.applicationuser', verbose_name='Client')),
                ('external_comm_external_followup_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='externalcm_external_followup_user', to='authentication.applicationuser', verbose_name='External Follow Up User')),
                ('external_comm_external_referral_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='externalcm_external_referral_user', to='authentication.applicationuser', verbose_name='External Follow Up User')),
            ],
        ),
    ]
