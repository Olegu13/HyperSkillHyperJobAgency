from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from vacancy.models import Vacancy
from resume.models import Resume

# Create your views here.

links_from_index = ['login', 'signup', 'vacancies', 'resumes', 'home', 'logout']


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'links': links_from_index})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class MyHomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {'username': request.user.get_username()}
        else:
            context = {'username': 'You are not logged In'}
        return render(request, 'home.html', context)


class MyResumeNew(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_staff:
                Resume.objects.create(description=request.POST.get('description'), author=request.user)
                return redirect('/home')
        raise PermissionDenied


class MyVacancyNew(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                Vacancy.objects.create(description=request.POST.get('description'), author=request.user)
                return redirect('/home')
        raise PermissionDenied
