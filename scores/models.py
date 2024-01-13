from django.db import models


class Point(models.Model):
    class Action(models.TextChoices):
        DEFAULT = ("_", "Select")
        HALF_TIME_PLAYED = ("HT", "Half Time Played")
        FULL_TIME_PLAYED = ("FT", "Full Time Played")
        GOAL = ("GS", "Goal Scored")
        ASSIST = ("AST", "Assist")
        CLEAN_SHEET = ("CS", "Clean Sheet")
        SAVES = ("3Sv", "3 Shots Saved")
        PENALTY_SAVED = ("PKSv", "Penalty Saved")
        PENALTY_MISSED = ("PKMs", "Penalty Missed")
        BONUS_POINTS = ("BSP", "Bonus Points")
        GOALS_CONCEDED = ("GC", "Goals Conceded")
        YELLOW_CARD = ("YC", "Yellow Card")
        RED_CARD = ("RC", "Red Card")
        OWN_GOAL = ("OG", "Own Goal")

    action = models.CharField(
        max_length=4,
        choices=Action.choices,
        default=Action.DEFAULT,
    )

    def __str__(self) -> str:
        pairs = dict(self.Action.choices)
        return f"{pairs.get(self.action)}"
