from django.urls import path
from puzzlehunt_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("puzzles/<int:puzzle_id>/", views.puzzle, name="puzzle"),
    path("submit/<int:puzzle_id>/<str:submission>", views.submit, name="submit"),
]
