# Generated by Django 3.2 on 2021-11-03 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casemanager', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreassessment',
            name='mode_of_assessment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientreassessment',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newemcassessment',
            name='mode_of_assessment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
