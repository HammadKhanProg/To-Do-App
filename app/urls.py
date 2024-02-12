from django.urls import path
from . import views
urlpatterns=[
    path("",views.Home,name="home"),
    path("updatetask/<pk>/",views.Updatetask,name="updatetask"),
    path("deletetask/<pk>/",views.deletetask,name="deletetask")
]