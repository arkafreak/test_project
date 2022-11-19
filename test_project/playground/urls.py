from django.urls import path
from . import views

#urlconfigmodule
urlpatterns = [
    path('hello/',views.say_hello)
    ]
