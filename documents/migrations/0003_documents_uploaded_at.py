# Generated by Django 3.2 on 2021-12-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_reviewboardreferralformsdocuments_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]