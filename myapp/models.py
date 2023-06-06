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
        verbose_name = 'Chelovek'
        verbose_name_plural = 'Ludi'

class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='marka')
    model = models.CharField(max_length=30, verbose_name='model')
    color = models.CharField(max_length=30, verbose_name='color')
    power = models.IntegerField(verbose_name='power')
    year = models.IntegerField(verbose_name='year')

    # def __str__(self):
    #     return ''.join([self.brand.name, self.model.name])
    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashiny'