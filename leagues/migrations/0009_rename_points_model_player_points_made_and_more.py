# Generated by Django 4.2.3 on 2024-02-08 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("leagues", "0008_rename_points_made_player_points_model"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player",
            old_name="points_model",
            new_name="points_made",
        ),
        migrations.RenameField(
            model_name="team",
            old_name="money_bank",
            new_name="budget",
        ),
        migrations.AddField(
            model_name="league",
            name="benchers_per_team",
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.AddField(
            model_name="league",
            name="is_locked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="league",
            name="max_selection_per_club",
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AddField(
            model_name="league",
            name="starter_per_team",
            field=models.PositiveIntegerField(default=11),
        ),
        migrations.AddField(
            model_name="league",
            name="teams_budget",
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.CreateModel(
            name="Transfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "player_bought",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="transfers",
                        to="leagues.player",
                    ),
                ),
                (
                    "player_sold",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="trasfers",
                        to="leagues.player",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trasfers",
                        to="leagues.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                (
                    "league",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="league",
                        to="leagues.league",
                    ),
                ),
            ],
        ),
    ]