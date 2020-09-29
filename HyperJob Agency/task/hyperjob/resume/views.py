from django.shortcuts import render
from django.views import View
from resume.models import Resume as resume_model_manager


# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resumes.html', context={'resumes': resume_model_manager.objects.all()})
