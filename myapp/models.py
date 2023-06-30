from django.urls import reverse

from django.db import models

#python manage.py makemigrations
#python manage.py migrate
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    age = models.IntegerField(verbose_name='age')
    city = models.CharField(max_length=100, verbose_name='city')
    is_activated = models.BooleanField(verbose_name='activation')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год выпуска')

    # def __str__(self):
    #     return ''.join([self.brand.name, self.model.name])
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл. почта')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Driver(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    experience = models.IntegerField(verbose_name='Опыт работы', null=False)
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    workplace = models.CharField(max_length=50, verbose_name='Предыдущее место работы')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Employee(models.Model):
    edu_choices = [('middle', 'среднее'),
                   ('high', 'высшее'),
                   ('professional', 'профессиональное')
                   ]

    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    position = models.CharField(max_length=50, verbose_name='Должность')
    education = models.CharField(max_length=50, choices=edu_choices)

    def __str__(self):
        return ' '.join([str(self.firstname), str(self.lastname)])

    def get_absolute_url(self):
        return reverse('employee_list')


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'



