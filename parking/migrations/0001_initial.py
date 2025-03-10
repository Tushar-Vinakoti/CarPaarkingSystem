# Generated by Django 5.1.4 on 2025-03-08 19:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('vehicle_number', models.CharField(max_length=20, unique=True)),
                ('registration_number', models.CharField(default='', max_length=50)),
                ('vehicle_type', models.CharField(choices=[('2W', 'Two Wheeler'), ('4W', 'Four Wheeler'), ('HV', 'Heavy Vehicle'), ('OT', 'Other')], default='OT', max_length=2)),
                ('entry_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('exit_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
