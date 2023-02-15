
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Project
from .serializers import UserSerializer, ProjectSerializer

@api_view(['POST'])
def getUID(req):
    uid = req.user.getID()


    return Response(uid)
    # return Response((UserSerializer(uid).data))

@api_view(['POST'])
def getProjects(req, id):
    # projects = User.objects.get(id=req.getID()).projects.all()
    projects = req.user.projects
    return Response(projects)

@api_view(['POST'])
def createProject(req, id):
    project = Project.objects.create(
        name=req.data["name"],
        owner=req.user,
        description=req.data["description"]
    )
    res = req.user.add_project(str(project.id))
    print(res)
    
    return Response(ProjectSerializer(project).data)