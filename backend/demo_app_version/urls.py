from django.urls import path
from demo_app_version import views

urlpatterns = [
  path('hello-world/', views.hello_world),
  path('custom-version/', views.DemoView.as_view()),
  path('another-custom-version/', views.AnotherView.as_view()),
]