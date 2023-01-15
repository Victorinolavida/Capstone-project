from django.urls import path
from .  import views

urlpatterns = [
    #path("", views.sayHello, name="say hello"),
    path("",views.index,name='index')
]