from django.urls import path, include
from .views import *

urlpatterns = [
    path("get/", getScripts),
    path("create/", createScript),
    path("<str:name>/", updateScript),


]
