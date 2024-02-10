from django.urls import path

from .views import (
    LeagueListView,
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
    # League model"
    path("", LeagueListView.as_view(), name="league_list"),
    path("create/", LeagueCreateView.as_view(), name="league_create"),
    path("delete/", LeagueDeleteView.as_view(), name="league_delete"),
    path("update/", LeagueUpdateView.as_view(), name="league_update"),
    path("<slug:slug>/", LeagueDetailView.as_view(), name="league_detail"),
    # Player model
    path("players-create/", PlayerCreateView.as_view(), name="player_create"),
    path("players-delete/", PlayerDeleteView.as_view(), name="players_delete"),
    path("players/<int:pk>", PlayerDetailView.as_view(), name="players_detail"),
    # PlayerPoint model
    path("players-point-create/", PlayerPointCreateView.as_view(), name="point_create"),
    path("players-point-delete/", PlayerPointDeleteView.as_view(), name="point_delete"),
    path("players-point-update/", PlayerPointUpdateView.as_view(), name="point_update"),
    path(
        "players-point/<int:pk>", PlayerPointDetailView.as_view(), name="point_detail"
    ),
]
