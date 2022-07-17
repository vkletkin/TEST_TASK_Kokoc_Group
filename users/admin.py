from itertools import count
from multiprocessing.connection import Client
from django.contrib import admin
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "points_count", "passed_tests", "color")
    empty_value_display = "-пусто-"


admin.site.register(Profile, ProfileAdmin)
