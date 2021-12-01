# Generated by Django 3.2 on 2021-11-28 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Message')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('sender_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('recipient_deleted_at', models.DateTimeField(blank=True, null=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-sent_at'],
            },
        ),
    ]
