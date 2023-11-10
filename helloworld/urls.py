from django.urls import path
from helloworld.views import index

urlpatterns = [
    path("", index),
]
