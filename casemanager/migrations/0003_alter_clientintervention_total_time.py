# Generated by Django 3.2 on 2022-01-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casemanager', '0002_auto_20220129_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientintervention',
            name='total_time',
            field=models.TextField(blank=True, null=True),
        ),
    ]