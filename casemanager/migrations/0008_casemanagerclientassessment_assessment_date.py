# Generated by Django 3.2 on 2021-12-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casemanager', '0007_auto_20211205_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemanagerclientassessment',
            name='assessment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]