# Generated by Django 5.1.7 on 2025-04-20 19:04

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votings', '0003_alter_voting_end_date_alter_voting_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 21, 19, 4, 7, 482305)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c8d846c0-176e-4fd1-90dd-abaedb025102'), editable=False, primary_key=True, serialize=False),
        ),
    ]
