from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/<int:page_number>/', views.persons, name='persons'),
    path('person/<int:person_id>/', views.person_page, name='person_page')
]