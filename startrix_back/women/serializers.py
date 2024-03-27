import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubRawUsers
        fields = ('name', 'location', 'avatar_url', 'socials', 'email')

