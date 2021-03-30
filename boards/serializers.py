from rest_framework import serializers
from . import models

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'username',
        )
        model = models.Board
