# Generated by Django 4.2.3 on 2024-02-08 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("leagues", "0012_alter_club_league"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="club",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="players",
                to="leagues.club",
            ),
        ),
    ]
