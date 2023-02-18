from .models import Script
from rest_framework.serializers import ModelSerializer


class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = ('id', 'name', 'project', 'nodes',
                  'edges', 'data', 'date_created')
