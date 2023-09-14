from django.contrib.auth.models import User
from django.db import models
import datetime

# freqChoices = [('ON', 'единоразовая'), ('DA', 'ежедневная'), ('WE', 'еженедельная'), ('MO', 'ежемесячная')]
sphereChoices = [('учеба', 'учеба'), ('работа', 'работа'), ('здоровье', 'здоровье'), ('хобби', 'хобби'), ('иное', 'иное')]
impChoices = [('желательно', 'желательно'), ('важно', 'важно'),
              ('критически важно', 'критически важно'), ('жизненно важно', 'жизненно важно')]


class Mission(models.Model):
    title = models.CharField(verbose_name='Задача', max_length=20)
    descr = models.CharField(verbose_name='Описание', null=True, max_length=50)
    # freq = models.CharField(verbose_name='Повторяемость', max_length=20, choices=freqChoices, default='ON')
    sphere = models.CharField(verbose_name='Сфера', max_length=20, choices=sphereChoices, default='иное')
    imp = models.CharField(verbose_name='Важность', max_length=20, choices=impChoices, default='желательно')
    deadline = models.DateField(verbose_name='Крайний срок')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    edit = "Edit"

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return self.title
