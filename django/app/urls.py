from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("api/", views.TestModelListView.as_view(), name="app_home"),
    path("api/<slug:slug>/", views.TestModel.as_view(), name="test_model"),
]