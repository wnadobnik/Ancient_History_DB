from django.db import models
import datetime

class Person(models.Model):
    name = models.CharField(max_length=120)

    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=120, blank=True, default=None)
    birth_upper = models.IntegerField(blank=True, default=None)
    birth_lower = models.IntegerField(blank=True, default=None)
    death_lower = models.IntegerField(blank=True, default=None)
    death_upper = models.IntegerField(blank=True, default=None)

    MALE = 'M'
    FEMALE = 'F'
    SEXES = ([MALE, 'Male'],(FEMALE, 'Female'))
    sex = models.CharField(max_length=2, choices=SEXES)


    def __str__(self):
        result = f'{self.name}'
        if self.city:
            result += f'from {self.city} in province {self.city.province}'
        return result

class City(models.Model):
    name = models.CharField(max_length=120)
    is_capital = models.BooleanField(default=False)

    province = models.ForeignKey('Province', on_delete=models.CASCADE)

    def __str__(self):
        result = self.name
        if self.is_capital:
            result += ', capital city'
        return result

class Province(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    # capital

#     events = models.ManyToManyField('HistoricEvent')
#
# class HistoricEvent(models.Model):
#     date = models.DateTimeField
#     participants = models.ManyToManyField('HistoricPerson')

# class Letter(models.Model):
#     authors
#     receivers
#     date
#     context
