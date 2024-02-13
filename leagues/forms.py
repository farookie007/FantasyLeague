from django import forms

from .models import Team


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            "name",
            "players",
            "captain",
            "vice_captain",
        )
        widgets = {
            "players": forms.CheckboxSelectMultiple,
        }




# select movies.title, movies.year, ratings.rating, ratings.votes from movies
# join ratings on movies.id = ratings.movie_id
# where movies.year >= 2021
# and ratings.votes >= 100000
# and ratings.rating >= 6.5
# order by ratings.votes desc, ratings.rating desc, movies.year asc
# limit 30;