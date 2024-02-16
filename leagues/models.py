import random
import string
from django import forms
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

from scores.models import Point


def generate_code(length: int = 6) -> str:
    """
    Generates and returns a code of `length` numbers which is a mixture of uppercase letters and digits.
    Params:
        :params length: the length of the code
    Returns:
        : the code as a string
    """
    seq = string.ascii_uppercase + string.digits
    while True:
        code = "".join(random.choices(seq, k=length))
        if League.objects.filter(code=code).count() == 0:
            break
    return code


class League(models.Model):
    title = models.CharField(max_length=50, blank=True, unique=False)
    code = models.CharField(
        max_length=10, unique=True, db_index=True, default=generate_code
    )
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="leagues"
    )
    max_selection_per_club = models.PositiveIntegerField(default=3)
    teams_budget = models.FloatField()
    starter_per_team = models.PositiveIntegerField(default=11)
    benchers_per_team = models.PositiveIntegerField(default=4)
    # no team should be editable once the league is locked
    is_locked = models.BooleanField(default=False)
    slug = models.SlugField(max_length=10, unique=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.host}"

    def save(self, *args, **kwargs):
        """
        Ensures that the number of benchers per team is not greater than 4.
        Ensures that the number of starters per team is not greater than 11.
        These are the regular rules for a standard fantasy match.
        """
        if not self.slug:
            self.slug = slugify(f"{self.title} {self.code}")
        if self.starter_per_team > 11:
            # do not save and raise error
            pass
        if self.benchers_per_team > 4:
            # do not save and raise error
            pass
        return super().save(*args, **kwargs)


class Club(models.Model):
    name = models.CharField(max_length=32, blank=False, unique=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="clubs")


class Player(models.Model):
    name = models.CharField(max_length=25, null=False, blank=True)
    price = models.FloatField(default=0)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="players")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="players")
    rating = models.FloatField(default=0)
    position = models.CharField(
        max_length=2,
        choices=(
            ("GK", "Goal Keeper"),
            ("DF", "Defender"),
            ("MF", "Midfielder"),
            ("FW", "Forward"),
        ),
        default="MF",
    )
    points_made = models.ManyToManyField(
        Point, related_name="players", through="PlayerPoint"
    )
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}[{self.position}]"

    def total_points(self) -> int:
        """Return the total points earned by the `Player` as an int.
        Returns: the total points"""
        sum((point.value for point in self.points.all()))


class PlayerPoint(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="points")
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=(("A", "Approved"), ("P", "Pending")), default="A"
    )
    value = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.point.action} - {self.value}"

    @property
    def action(self):
        """Defines the responsible for this point.
        Returns:
            the action of the associated point."""
        return self.point.action

    def reward_GS(self):
        if self.player.position in ("GK", "DF"):
            reward = 6
        elif self.player.position == "MF":
            reward = 5
        elif self.player.position == "FW":
            reward = 4
        else:
            reward = 0
        return reward

    def reward_CS(self):
        if self.player.position in ("GK", "DF"):
            reward = 4
        elif self.player.position == "MF":
            reward = 1
        else:
            reward = 0
        return reward

    def save(self, *args, **kwargs):
        value_system = {
            "HT": 1,
            "FT": 2,
            "GS": self.reward_GS(),
            "AST": 3,
            "CS": self.reward_CS(),
            "3Sv": 1,
            "PKMs": -2,
            "BSP": 2,
            "GC": -1,
            "YC": -1,
            "RC": -3,
            "OG": -2,
        }
        self.value = value_system.get(self.point.action, 0)
        return super().save(*args, **kwargs)


class Team(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    budget = models.FloatField(default=100)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teams"
    )
    players = models.ManyToManyField(Player, related_name="teams")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")
    captain = models.ForeignKey(
        Player, on_delete=models.DO_NOTHING, related_name="caps", null=True
    )
    vice_captain = models.ForeignKey(
        Player, on_delete=models.DO_NOTHING, related_name="vice_caps", null=True
    )
    # total_pts = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.manager.username} - ${self.budget:.2f}"

    @property
    def total_points(self) -> int:
        """The total points that a team has"""
        return sum((player.total_points for player in self.players.all()))

    def save(self, *args, **kwargs):
        if self.name == "":
            self.name == self.manager.username
        try:
            self.captain, self.vice_captain = random.choices(self.players, k=2)
        except:
            pass
        return super().save(*args, **kwargs)


class Transfer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="transfers")
    player_sold = models.ForeignKey(
        Player, on_delete=models.DO_NOTHING, related_name="sold"
    )
    player_bought = models.ForeignKey(
        Player, on_delete=models.DO_NOTHING, related_name="bought"
    )
    time = models.DateTimeField(auto_now_add=True)
