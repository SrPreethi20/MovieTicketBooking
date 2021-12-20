from django.contrib.auth.models import User
from .models import Movie
from django.contrib.auth.models import User
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    #  To get object from foreign key
    # author_name = serializers.CharField(source='author.username')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'content', 'img', 'status']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']
