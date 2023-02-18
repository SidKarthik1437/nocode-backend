

class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = ('id', 'name', 'project', 'nodes',
                  'edges', 'data', 'date_created')
