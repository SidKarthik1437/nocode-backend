
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Project, Script
# from .serializers import UserSerializer, ProjectSerializer, ScriptSerializer
from .serializers import *

from rest_framework.decorators import authentication_classes, permission_classes


@api_view(['POST'])
def getUID(req):
    uid = req.User.getName()

    return Response(uid)
    # return Response((UserSerializer(uid).data))


@api_view(['GET'])
def getProjects(req, username):
    # projects = User.objects.get(id=req.getID()).projects.all()
    projects = Project.objects.filter(
        owner=User.objects.get(username=username)
    )
    res = []
    for i in projects:
        res.append(ProjectSerializer(i).data)
    return Response(res)


@api_view(['POST'])
def createProject(req, username):
    project = Project.objects.create(
        name=req.data['name'],
        description=req.data['description'],
        owner=User.objects.get(username=username))

    return Response(ProjectSerializer(project).data)


