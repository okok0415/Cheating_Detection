from rest_framework import serializers
from . import models


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "content",
            "user",
        )
        model = models.Board
