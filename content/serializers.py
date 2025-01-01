from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from content.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    @staticmethod
    def validate_file(file):
        if file.size > settings.DATA_UPLOAD_MAX_FILE_SIZE:
            raise ValidationError(f"File size exceeds the {settings.DATA_UPLOAD_MAX_FILE_SIZE/1024} MB limit.")
        if not file.name.endswith('.csv'):
            raise ValidationError("Invalid file format. Please upload a CSV file.")
        return file