from django.urls import path
from demo_app import views

urlpatterns = [
  path('hello-world/', views.hello_world)
]