from rest_framework import serializers
from .models import Citation, Synopsis, CustomUser, Challenge, Vitesse

class CitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citation
        fields = ['id', 'perso_name', 'anime_name', 'url', 'text']

class SynopsisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synopsis
        fields = ['id', 'url', 'anime', 'texte', 'validate']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'text', 'anime', 'texte', 'validate']

class VitesseSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    challenge = ChallengeSerializer(required=False)
    synopsis = SynopsisSerializer(required=False)
    citation = CitationSerializer(required=False)

    class Meta:
        model = Vitesse
        fields = ['id', 'user', 'challenge', 'synopsis', 'citation', 'speed']


from rest_framework import serializers
from django.contrib.auth.models import User

