from rest_framework import serializers
from apps.main.models import News


class NewsDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'created_at')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'description', 'created_at')