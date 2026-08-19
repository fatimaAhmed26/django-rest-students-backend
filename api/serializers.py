from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    favoriteFood = serializers.CharField(source='favorite_food')
    favoriteEmoji = serializers.CharField(source='favorite_emoji')

    class Meta:
        model = Student
        fields = ['id', 'name', 'favoriteFood', 'favoriteEmoji']