from django.urls import path
from . import views

urlpatterns = [
    path("playstation-games", views.list_games),
    path("playstation-games/<id>", views.retrieve_game),
]
