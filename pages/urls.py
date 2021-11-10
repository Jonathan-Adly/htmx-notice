from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("form-1", views.form_1, name="form_1"),
    path("form-2", views.form_2, name="form_2"),
]
