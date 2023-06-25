from rest_framework import serializers

from baseapp.models import Project
from rest_framework.response import Response



class ProjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created', 'updated']


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):
        name = str(validated_data['file'])
        id_project = self.get_project_from_file(name)
        project = Project.objects.filter(id=id_project).first()
        if not project:
            return Response({'error': f'проекта с номеро {id_project} нет'})
        print(project)
        return project
    

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created', 'updated']
