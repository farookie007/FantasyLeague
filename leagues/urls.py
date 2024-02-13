from django.urls import path

from .views import (
    LeagueListView,
    LeagueCreateView,
    LeagueDeleteView,
    LeagueUpdateView,
    LeagueDetailView,
    # Team
    TeamCreateView,
)


app_name = "leagues"

urlpatterns = [
    # League model"
    path("", LeagueListView.as_view(), name="league_list"),
    path("create/", LeagueCreateView.as_view(), name="league_create"),
    path("<slug:slug>/", LeagueDetailView.as_view(), name="league_detail"),
    path(
        "<slug:slug>/delete/",
        LeagueDeleteView.as_view(),
        name="league_delete",
    ),
    path(
        "<slug:slug>/update/",
        LeagueUpdateView.as_view(),
        name="league_update",
    ),

    # Team model
    path(
        "<slug:league_slug>/team-create/",
        TeamCreateView.as_view(),
        name="team_create",
    ),
]
