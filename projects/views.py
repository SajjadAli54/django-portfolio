from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from projects.models import Project

# Create your views here.

def project_index(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return render(request, 'projects/project_index.html', {'projects': projects})

def project_detail(request: HttpRequest, pk: int) -> HttpResponse:
    project = Project.objects.filter(pk=pk).first()
    return render(request, 'projects/project_detail.html', {'project': project})