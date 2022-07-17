from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("list/", views.get_to_do_list, name="list"),
    path("task/<id>", views.get_to_do_task, name="task"),
    path("add/", views.add_to_do_task, name="add"),
    path("delete/<id>", views.delete_to_do_task, name="delete"),
    path("update/<id>", views.update_to_do_task, name="update")
]
