# Generated by Django 2.2 on 2022-07-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='isRight',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Ваш ответ'),
        ),
    ]
