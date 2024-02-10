# Generated by Django 4.2.3 on 2024-02-08 02:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leagues", "0010_remove_league_max_selection_per_club"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="max_selection_per_club",
            field=models.PositiveIntegerField(default=3),
        ),
    ]