# Generated by Django 3.2 on 2021-10-26 18:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentFormsDocuments',
            fields=[
                ('assessment_form_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_provider_form', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('document_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('path', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentTypes',
            fields=[
                ('type_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('type_label', models.TextField()),
                ('type_code', models.TextField()),
            ],
            options={
                'verbose_name': 'Document Type',
                'verbose_name_plural': 'Document Types',
            },
        ),
        migrations.CreateModel(
            name='ExistingClientCommunityParamedicFormsDocuments',
            fields=[
                ('form_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterventionFormsDocuments',
            fields=[
                ('intervention_form_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewClientCommunityParamedicFormsDocuments',
            fields=[
                ('form_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewBoardReferralFormsDocuments',
            fields=[
                ('referral_form_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]