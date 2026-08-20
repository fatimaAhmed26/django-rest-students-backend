from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)
    favoriteFood = serializers.CharField(source='favorite_food')
    favoriteEmoji = serializers.CharField(source='favorite_emoji')
    createdAt = serializers.DateTimeField(
        source="created_at",
        read_only=True,
    )

    class Meta:
        model = Student
        fields = ['_id', 'name', 'favoriteFood', 'favoriteEmoji', 'createdAt']