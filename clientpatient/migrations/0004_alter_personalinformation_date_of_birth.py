# Generated by Django 3.2 on 2022-01-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpatient', '0003_alter_personalinformation_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='date_of_birth',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]