from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.todo,name="todo"),
    path("dash/",views.dash,name="dash"),
    path("create/",views.create,name="create"),
    path("read/",views.read,name="read"),
    path("delete/<int:id>/",views.delete_1,name="delete_1"),
    path("update/<int:id>/",views.update_1,name="update_1")
]