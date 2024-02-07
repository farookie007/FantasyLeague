from django.urls import path

from .views import (
    LeagueCreateView,
    LeagueDeleteView,
    LeagueUpdateView,
    LeagueDetailView,
    PlayerCreateView,
    PlayerDeleteView,
    PlayerDetailView,
    PlayerPointCreateView,
    PlayerPointDeleteView,
    PlayerPointUpdateView,
    PlayerPointDetailView,
)


app_name = "leagues"

urlpatterns = [
    path("create/", LeagueCreateView.as_view, name="league_create"),
]
