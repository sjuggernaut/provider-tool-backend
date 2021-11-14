# Generated by Django 3.2 on 2021-11-06 22:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientReAssessment',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('total_time', models.TimeField()),
                ('mode_of_assessment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExistingEMCAssessment',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewEMCAssessment',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('total_time', models.TimeField()),
                ('mode_of_assessment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]