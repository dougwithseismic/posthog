# Generated by Django 3.2.5 on 2021-11-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0180_person_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="correlation_config",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
