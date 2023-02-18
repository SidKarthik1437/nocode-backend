
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Project, User
from .models import Script
# from .serializers import UserSerializer, ProjectSerializer, ScriptSerializer
from .serializers import *

from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.


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
