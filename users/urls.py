from django.urls import path
from users.views import SignUp, show_users 

urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("show_users/", show_users, name="show_users")
]