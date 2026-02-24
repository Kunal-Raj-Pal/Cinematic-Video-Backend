from django.urls import path
from .views import addProject,seeProjects,deleteProject, Dashboard

urlpatterns = [
    path('api/projects',seeProjects,name='seeProjects'),
    path('api/add/project',addProject,name='addProject'),
    path('',Dashboard,name='dashboard'),
    path('api/delete/project/<str:id>',deleteProject,name='deleteProject'),
]
