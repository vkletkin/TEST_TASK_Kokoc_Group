from django.shortcuts import render
from quiz.models import Quiz


def show_tests(request):
    tests = Quiz.objects.all()[:10]
    return render(request, "show_tests.html", {"tests": tests})
