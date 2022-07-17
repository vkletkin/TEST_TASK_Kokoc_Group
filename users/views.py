from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CreationForm
from users.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


def show_users(request):
    users = Profile.objects.order_by("-points_count")[:10]
    return render(request, "show_users.html", {"users": users})


def add_points(count):
    Profile.objects.filter(user=User).update(
        points_count=F('points_count') + count)
    return


def subtract_points(count):
    Profile.objects.filter(user=User).update(
        points_count=F('points_count') - count)
    return


def check_points():
    user = Profile.objects.get(user=User)
    return user.points_count


def subtract_points(count):
    Profile.objects.filter(user=User).update(
        points_count=F('passed_tests') + count)
    return


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def form_valid(self, form):

        #profile = Profile.objects.create(user=User)
        return super().form_valid(form)
