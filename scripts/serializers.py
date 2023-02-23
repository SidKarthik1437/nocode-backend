from .models import Script
from rest_framework.serializers import ModelSerializer


class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'
