from django.urls import path
from .views import *

urlpatterns = [
    path("getuser/", getUID),
    path("<int:id>/", getProjects),
    path("<int:id>/create-project", createProject),
    
]
