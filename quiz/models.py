from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название теста')
    questions_count = models.PositiveIntegerField(verbose_name='Количество вопросов',default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, verbose_name='Тест')
    text = models.TextField(verbose_name='Текст вопроса', default="Ваш вопрос")
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name='Вопрос')
    text = models.CharField(max_length=300,verbose_name='Ваш ответ')
    isRight = models.BooleanField(default=False,verbose_name='Правильный ответ')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class ResultQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест')
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')   
    dateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    rating = models.FloatField(verbose_name="Кол-во балов за тест")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
