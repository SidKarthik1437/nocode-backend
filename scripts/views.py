
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Project, Script
# from .serializers import UserSerializer, ProjectSerializer, ScriptSerializer
from .serializers import *

from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.


@api_view(['POST'])
def createScript(req, username, project):
    script = Script.objects.create(
        name=req.data['name'],
        project=Project.objects.get(name=project)
    )

    return Response(ScriptSerializer(script).data)
