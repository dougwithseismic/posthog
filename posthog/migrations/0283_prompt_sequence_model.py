# Generated by Django 3.2.16 on 2022-12-06 09:32

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0282_fix_insight_caching_state_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prompt",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("step", models.IntegerField()),
                ("type", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("text", models.CharField(max_length=1000)),
                ("placement", models.CharField(default="top", max_length=200)),
                ("buttons", models.JSONField()),
                (
                    "reference",
                    models.CharField(default=None, max_length=200, null=True),
                ),
                ("icon", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="PromptSequence",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
                (
                    "path_match",
                    django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
                ),
                (
                    "path_exclude",
                    django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
                ),
                ("status", models.CharField(max_length=200)),
                ("requires_opt_in", models.BooleanField(default=False)),
                ("autorun", models.BooleanField(default=True)),
                (
                    "must_have_completed",
                    models.ManyToManyField(blank=True, to="posthog.PromptSequence"),
                ),
                ("prompts", models.ManyToManyField(to="posthog.Prompt")),
            ],
        ),
        migrations.CreateModel(
            name="UserPromptState",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_updated_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("step", models.IntegerField(default=None, null=True)),
                ("completed", models.BooleanField(default=False)),
                ("dismissed", models.BooleanField(default=False)),
                (
                    "sequence",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.promptsequence",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="UserPromptSequenceState",
        ),
        migrations.AddConstraint(
            model_name="userpromptstate",
            constraint=models.UniqueConstraint(fields=("user", "sequence"), name="unique_user_prompt_state"),
        ),
        migrations.AddConstraint(
            model_name="promptsequence",
            constraint=models.UniqueConstraint(fields=("key",), name="unique_prompt_sequence"),
        ),
    ]
