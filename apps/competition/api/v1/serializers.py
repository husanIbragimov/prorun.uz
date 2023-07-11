from rest_framework import serializers
from apps.competition.models import Category, Competition, CompetitionDetail, Participant, TextDetail


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'icon')


class TextDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextDetail
        fields = ('id', 'title', 'description')


class CompetitionDetailSerializer(serializers.ModelSerializer):
    texts = TextDetailSerializer(many=True)
    competition = serializers.CharField(source='competition.title')

    class Meta:
        model = CompetitionDetail
        fields = ('id', 'competition', 'title', 'image', 'texts')


class CompetitionSerializer(serializers.ModelSerializer):
    competition_details = CompetitionDetailSerializer(many=True)

    class Meta:
        model = Competition
        fields = (
            'id', 'category', 'title', 'image', 'start_date', 'end_date', 'distance', 'status', 'period', 'members',
            'free_places', 'time_limit', 'competition_details')
