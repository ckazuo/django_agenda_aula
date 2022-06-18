from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("agenda", views.agenda_view, name="agenda"),
    path("calendar", views.calendar_view, name="calendar"),
    path("marcar", views.marcar_view, name="marcar"),
]