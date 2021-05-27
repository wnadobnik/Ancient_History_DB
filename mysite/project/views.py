from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Person
from math import ceil

def index(request):

    template = loader.get_template('project/index.html')
    return HttpResponse(template.render({}, request))


def persons(request, page_number):
    page_limit = 10
    pages_count = range(1, ceil(Person.objects.count() / page_limit) + 1)
    lower_limit = (page_number - 1) * page_limit if page_number != 1 else 0
    upper_limit = page_number * page_limit
    persons = Person.objects.all()[lower_limit:upper_limit]

    return render(request, 'project/persons.html', {'persons': persons, 'pages_count': pages_count})

def person_page(request, person_id):

    if not Person.objects.filter(id=person_id).exists():
        person = Person.objects.first()
    else:
        person = Person.objects.get(id=person_id)
    return render(request, 'project/person.html', {'person': person})