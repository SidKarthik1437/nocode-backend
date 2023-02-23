
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Project, User
from .models import Script
# from .serializers import UserSerializer, ProjectSerializer, ScriptSerializer
from .serializers import *

from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.

from .execution import *


@api_view(['GET'])
def getScripts(req, username, project):

    scripts = Script.objects.filter(
        project=Project.objects.get(name=project),
        owner=User.objects.get(username=username)
    )
    res = []

    for script in scripts:
        res.append(ScriptSerializer(script).data)
    print(res)
    return Response(res)


@api_view(['POST'])
def createScript(req, username, project):
    script = Script.objects.create(
        name=req.data['name'],
        project=Project.objects.get(name=project),
        owner=User.objects.get(username=username),
    )

    return Response(ScriptSerializer(script).data)


@api_view(['POST'])
def updateScript(req, username, project, name):
    script = Script.objects.get(
        name=name,
        project=Project.objects.get(name=project),
        owner=User.objects.get(username=username),
    )

    #script.name = req.data['name']
    script.nodes = req.data['nodes']
    script.edges = req.data['edges']
    script.save()

    return Response(ScriptSerializer(script).data)


@api_view(['GET'])
def executeScript(req, username, project, name):

    script = Script.objects.get(
        name=name,
        project=Project.objects.get(name=project),
        owner=User.objects.get(username=username),
    )
    res = process(ScriptSerializer(script).data)

    return Response(res)
