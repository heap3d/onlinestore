from django.urls import path
from hello.views import say_hello, helloworld, index

urlpatterns = [
    path("hello/", say_hello),
    path("helloworld/", helloworld),
    path("", index),
]
