from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update-table/<int:form_num>", views.update_table, name="update_table"),
    path("form/<int:form_num>", views.form, name="form"),
    path("generate-pdf", views.generate_pdf, name="generate_pdf"),
]
