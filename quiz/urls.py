from django.urls import path
from quiz.views import show_tests


urlpatterns = [
    path("show_tests/", show_tests, name="show_tests"),
]
