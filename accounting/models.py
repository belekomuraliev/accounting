from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    title = models.CharField(max_length=50, verbose_name="Должность")
    department = models.CharField(max_length=50, verbose_name="Отдел")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Employees(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    salary = models.FloatField(verbose_name="Зарплата")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'Сотрудник {self.fullname} занимает должность {self.position.title}'



