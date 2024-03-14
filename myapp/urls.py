from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.test1,name="test1"),
    path("dash/",views.test2,name="test2"),
    path("form/",views.test3,name="test3"),
    path("child/",views.test4,name="test4"),
]