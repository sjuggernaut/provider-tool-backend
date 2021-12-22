# Generated by Django 3.2 on 2021-12-22 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('clientpatient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientVitalSigns',
            fields=[
                ('vital_signs_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bp_value', models.TextField(blank=True, null=True)),
                ('pulse_value', models.TextField(blank=True, null=True)),
                ('hr_value', models.TextField(blank=True, null=True)),
                ('rr_value', models.TextField(blank=True, null=True)),
                ('temp_value', models.TextField(blank=True, null=True)),
                ('weight_value', models.TextField(blank=True, null=True)),
                ('oximetry_choice', models.TextField(blank=True, null=True)),
                ('oximetry_value', models.TextField(blank=True, null=True)),
                ('last_weight', models.TextField(blank=True, null=True)),
                ('last_weight_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityParamedicUser',
            fields=[
                ('community_paramedic_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.PROTECT, related_name='communityparamedicuser', to=settings.AUTH_USER_MODEL, verbose_name='User - Community Paramedic')),
            ],
            options={
                'verbose_name': 'Community Paramedic',
                'verbose_name_plural': 'Community Paramedics',
            },
        ),
        migrations.CreateModel(
            name='ExistingCaseClientAssessmentChangeInCondition',
            fields=[
                ('change_in_condition_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mental_status_changes', models.TextField()),
                ('functional_status_changes', models.TextField()),
                ('respiratory_changes', models.TextField()),
                ('gi_abdomen_changes', models.TextField()),
                ('gi_abdomen_changes_detail', models.TextField(blank=True, null=True)),
                ('gu_urine_changes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewCaseClientAssessment',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('departure_time', models.TimeField(blank=True, null=True)),
                ('priority_problems', models.TextField(blank=True, null=True)),
                ('priority_problems_detail', models.TextField(blank=True, null=True)),
                ('interventions', models.TextField(blank=True, null=True)),
                ('interventions_detail', models.TextField(blank=True, null=True)),
                ('recommendations', models.TextField(blank=True, null=True)),
                ('recommendations_detail', models.TextField(blank=True, null=True)),
                ('risks_changes_reported_to_emp', models.BooleanField(default=False)),
                ('reported_provider_name', models.ForeignKey(db_column='reported_provider', on_delete=django.db.models.deletion.PROTECT, to='users.users', verbose_name='Provider')),
                ('vital_signs', models.ForeignKey(db_column='vital_signs', on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.clientvitalsigns', verbose_name='Vital Signs')),
            ],
        ),
        migrations.CreateModel(
            name='HomeSafetyAssessment',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('question', models.TextField()),
                ('answer', models.IntegerField(default=False)),
                ('answer_detail', models.TextField(blank=True, null=True)),
                ('new_client_assessment', models.ForeignKey(db_column='new_client_assessment', default=None, on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.newcaseclientassessment', verbose_name='New Case Client Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='ExistingCaseClientAssessment',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('departure_time', models.TimeField(blank=True, null=True)),
                ('assessment_change_in_condition', models.BooleanField(default=False)),
                ('assessment_change_in_condition_detail', models.TextField(blank=True, null=True)),
                ('assessment_changes_perceived_date', models.DateField(blank=True, null=True)),
                ('assessment_condition_worse_reasons', models.TextField(blank=True, null=True)),
                ('assessment_condition_better_reasons', models.TextField(blank=True, null=True)),
                ('assessment_condition_occurred_before', models.BooleanField(default=False)),
                ('assessment_treatment_last_episode', models.TextField(blank=True, null=True)),
                ('assessment_other_information', models.TextField(blank=True, null=True)),
                ('priority_problems', models.TextField(blank=True, null=True)),
                ('priority_problems_detail', models.TextField(blank=True, null=True)),
                ('interventions', models.TextField(blank=True, null=True)),
                ('interventions_detail', models.TextField(blank=True, null=True)),
                ('recommendations', models.TextField(blank=True, null=True)),
                ('recommendations_detail', models.TextField(blank=True, null=True)),
                ('risks_changes_reported_to_emp', models.BooleanField(default=False)),
                ('changes_in_condition', models.ForeignKey(db_column='condition_changes', on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.existingcaseclientassessmentchangeincondition', verbose_name='Changes in Condition')),
                ('reported_provider_name', models.ForeignKey(db_column='reported_provider', on_delete=django.db.models.deletion.PROTECT, to='users.users', verbose_name='Provider')),
                ('vital_signs', models.ForeignKey(db_column='vital_signs', on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.clientvitalsigns', verbose_name='Vital Signs')),
            ],
        ),
        migrations.CreateModel(
            name='DailyWorkLoad',
            fields=[
                ('daily_workload_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('daily_workload_date', models.DateField(blank=True, null=True)),
                ('client_caseload_casemanagement_number_clients', models.IntegerField(null=True)),
                ('client_caseload_casemanagement_total_time', models.TimeField()),
                ('client_caseload_regular_number_clients', models.IntegerField(null=True)),
                ('client_caseload_regular_total_time', models.TimeField()),
                ('community_paramedic', models.ForeignKey(blank=True, db_column='community_paramedic', null=True, on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.communityparamedicuser', verbose_name='Community Paramedic')),
            ],
            options={
                'verbose_name': 'Daily Workload',
                'verbose_name_plural': 'Daily Workloads',
            },
        ),
        migrations.CreateModel(
            name='CommunityClientAssessment',
            fields=[
                ('client_assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('client_status', models.CharField(blank=True, choices=[('EXISTING_CASE_MANAGEMENT_CLIENT', 'Existing Case Management Client'), ('NEW_CASE_MANAGEMENT_CLIENT', 'New Case Management Client')], default='NEW_CASE_MANAGEMENT_CLIENT', max_length=100)),
                ('client', models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.PROTECT, to='clientpatient.client', verbose_name='Assessment Client')),
                ('community_paramedic', models.ForeignKey(db_column='community_paramedic', on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.communityparamedicuser', verbose_name='Community Paramedic')),
                ('existing_case_client_assessment', models.ForeignKey(blank=True, db_column='existing_case_client_assessment', null=True, on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.existingcaseclientassessment', verbose_name='Existing Case Client Assessment')),
                ('new_case_client_assessment', models.ForeignKey(blank=True, db_column='new_case_client_assessment', null=True, on_delete=django.db.models.deletion.PROTECT, to='communityparamedic.newcaseclientassessment', verbose_name='New Case Management Client Assessment')),
            ],
        ),
    ]
