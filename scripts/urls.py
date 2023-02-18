from django.urls import path, include
from .views import *

urlpatterns = [
    path("", getScripts),
    path("create/", createScript),
    # path("<str:username>/<str:project>/", include('scripts.urls')),
    # path("<str:username>/<str:project>//", createScript),

]
