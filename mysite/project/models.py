from django.db import models


class HistoricPerson(models.Model):
    name = models.CharField(max_length=120)

    province = models.CharField(max_length=120, null=True)
    role = models.CharField(max_length=120, null=True)

    MALE = 'M'
    FEMALE = 'F'
    SEXES = ([MALE,'Male'],(FEMALE,'Female'))
    sex = models.CharField(max_length=2, choices=SEXES)


    def __str__(self):
        presentation = '{self.name} from {self.province}'.format(self=self)
        return presentation



#     events = models.ManyToManyField('HistoricEvent')
#
# class HistoricEvent(models.Model):
#     date = models.DateTimeField
#     participants = models.ManyToManyField('HistoricPerson')
