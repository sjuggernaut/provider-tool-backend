# Generated by Django 3.2 on 2022-02-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinician', '0011_auto_20220204_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicianclientinterventions',
            name='date',
            field=models.TextField(blank=True, null=True),
        ),
    ]
