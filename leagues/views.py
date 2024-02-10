from typing import Any
from django.contrib import messages
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.text import slugify

from .models import League, Team, Player, PlayerPoint


class LeagueListView(ListView):
    model = League
    context_object_name = "leagues"
    template_name = "leagues/league_list.html"


class LeagueCreateView(LoginRequiredMixin, CreateView):
    model = League
    context_object_name = "league"
    template_name = "leagues/league_create.html"
    # success_url = reverse_lazy("leagues:league_list")
    queryset = League.objects.all()
    fields = (
        "title",
        "teams_budget",
        "starter_per_team",
        "benchers_per_team",
    )

    def get_success_url(self) -> str:
        obj = self.object
        return reverse_lazy("leagues:league_detail", kwargs={"title": slugify(obj.title), "slug": obj.slug})

    def form_valid(self, form):
        league = form.save(commit=False)
        league.host = self.request.user
        league.slug = slugify(league.code)
        league.save()
        messages.success(self.request, "League created successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid parameters")
        return super().form_invalid(form)


class LeagueDetailView(DetailView):
    model = League
    template_name = "leagues/league_detail.html"
    context_object_name = "league"



class LeagueUpdateView(UpdateView):
    model = League
    context_object_name = "league"
    template_name = "leagues/league_update.html"
    success_url = reverse_lazy("leagues:league_update")

    def get_success_url(self) -> str:
        obj = self.object
        return reverse_lazy("leagues:league_detail", kwargs={"title": slugify(obj.title), "slug": obj.slug})


class LeagueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = League
    template_name = "leagues/object_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self) -> bool | None:
        """Only the host of the league can delete."""
        return self.request.user == self.host


class PlayerCreateView(CreateView):
    """View for creating a `Player`"""

    model = Player
    context_object_name = "player"
    template_name = "leagues/player_create.html"
    success_url = reverse_lazy("leagues:league_detail")
    fields = (
        "name",
        "league",
        "club",
        "position",
    )

    def form_valid(self, form):
        messages.success(self.request, "Player registered")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Invalid entry. Retry.")
        return super().form_invalid(form)


class PlayerDetailView(DetailView):
    """View for displaying a `Player` information"""

    model = Player
    template_name = "leagues/player_detail.html"


class PlayerUpdateView(UpdateView):
    """View for updating a `Player`"""

    model = Player
    template_name = "leagues/player_create.html"
    fields = (
        "price",
        "flagged",
    )

    def form_valid(self, form):
        messages.success("Player Updated")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Error. Retry.")
        return super().form_invalid(form)


class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "leagues/object_delete.html"


class TeamCreateView(CreateView):
    model = Team
    context_object_name = "team"
    template_name = "leagues/team_create.html"
    success_url = reverse_lazy("leagues:team_detail")
    fields = (
        "name",
        "players",
        "captain",
        "vice_captain",
    )

    def form_valid(self, form):
        messages.success(self.request, "Player registered")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error("Invalid entry. Retry.")
        return super().form_invalid(form)


class TeamUpdateView(UpdateView):
    ...


class TeamDetailView(DetailView):
    ...


class TeamDeleteView(DeleteView):
    ...


class PlayerPointCreateView(CreateView):
    ...


class PlayerPointUpdateView(UpdateView):
    ...


class PlayerPointDetailView(DetailView):
    ...


class PlayerPointDeleteView(DeleteView):
    ...
