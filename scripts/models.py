from django.db import models

# Create your models here.
import jsonfield
from django.utils import timezone
from users.models import Project, User


class Script(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nodes = jsonfield.JSONField(blank=True, null=True)
    edges = jsonfield.JSONField(blank=True, null=True)
    data = jsonfield.JSONField(blank=True, null=True)
    date_created = timezone.now()

    def __str__(self):
        return self.name

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

    def getData(self):
        return self.edges
