from django.contrib import admin
from quiz.models import Answer, Question, Quiz, ResultQuiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "questions_count", "owner")
    search_fields = ("pk", "title", "questions_count", "owner")
    empty_value_display = "-пусто-"


admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("pk", "quiz", "text")
    empty_value_display = "-пусто-"


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("pk", "question", "text")
    empty_value_display = "-пусто-"


admin.site.register(Answer, AnswerAdmin)


class ResultQuizAdmin(admin.ModelAdmin):
    list_display = ("pk", "quiz", "user", "dateTime", "rating")
    search_fields = ("pk", "name", "user")
    empty_value_display = "-пусто-"


admin.site.register(ResultQuiz, ResultQuizAdmin)
