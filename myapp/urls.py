from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.todo,name="todo"),
    path("dash/",views.dash,name="dash"),
    path("form/",views.form,name="form"),
    path("data/",views.data,name="data"),
    path("delete/<int:obj_id>",views.delete_1,name="delete_1"),
    path("update/<int:obj_id>/",views.update_1,name="update_1")
]