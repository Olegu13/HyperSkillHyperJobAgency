from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy as vacancy_model_manager


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancyes.html', context={'vacancyes': vacancy_model_manager.objects.all()})
