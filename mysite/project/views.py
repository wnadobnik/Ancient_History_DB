from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import HistoricPerson
from math import ceil

def index(request):

    template = loader.get_template('project/index.html')
    return HttpResponse(template.render({}, request))


def persons(request, page_number):

    persons = HistoricPerson.objects.all()
    pages_count = range(1, ceil((persons.count() / 10)+1))
    lower_limit = (page_number-1)*10 if page_number != 1 else 0
    upper_limit = page_number*10
    persons = persons[lower_limit:upper_limit]

    return render(request, 'project/persons.html', {'persons': persons, 'pages_count': pages_count})


def person_page(request, person_id):

    if not HistoricPerson.objects.filter(id=person_id).exists():
        person = HistoricPerson.objects.first()
    else:
        person = HistoricPerson.objects.get(id=person_id)
    return render(request, 'project/person.html', {'person': person})