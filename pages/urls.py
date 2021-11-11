from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update-table/<int:form_num>", views.update_table, name="update_table"),
    path("form-1", views.form_1, name="form_1"),
    path("form-2", views.form_2, name="form_2"),
    path("form-3", views.form_3, name="form_3"),
    path("form-4", views.form_4, name="form_4"),
    path("form-5", views.form_5, name="form_5"),
    path("form-6", views.form_6, name="form_6"),
    path("form-7", views.form_7, name="form_7"),
    path("form-8", views.form_8, name="form_8"),
    path("form-9", views.form_9, name="form_9"),
    path("form-10", views.form_10, name="form_10"),
]
