from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Projects
from cloudinary.exceptions import Error as cloudinaryError
import requests

# Create your views here.
def seeProjects(req):
    project = Projects.objects.all()
    data = serializers.serialize('json', project)
    return HttpResponse(data, content_type='application/json')

def addProject(req):
    context = {'msg':""}
    if req.method == 'POST':
        name = req.POST.get('name')
        description = req.POST.get('description')
        image = req.FILES.get('image')

        try:
            project = Projects(name=name, description=description, image=image)
            project.save()
            context = {'msg':"Project added successfully✅"}
            return redirect('dashboard')

        except (requests.exceptions.ConnectionError, cloudinaryError):
            context['msg'] = 'Internet Connection Error, Turn on internet and try again.'

        except Exception as e:
            context['msg'] = f'Something went wrong: {str(e)}'
    return render(req,'addProjects.html',context)

def Dashboard(req):
    project = Projects.objects.all().values()
    context = {'project':project}
    print(project)
    return render(req,"dashboard.html",context)

def deleteProject(req, id):
    project = Projects.objects.get(pk=id)
    project.delete()
    return redirect('dashboard')