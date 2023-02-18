from django.urls import path, include
from .views import *

urlpatterns = [
    path("getuser/", getUID),
    path("<str:username>/", getProjects),
    path("<str:username>/create/", createProject),
    # path("<str:username>/<str:project>/", include('scripts.urls')),
    # path("<str:username>/<str:project>//", createScript),

]
