from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('connect4/', views.connect4_board, name='connect4_board'),
]