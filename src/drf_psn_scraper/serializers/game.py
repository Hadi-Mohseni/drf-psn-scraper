from rest_framework import serializers
from .edition import EditionSerializer


class GameCardSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.CharField()


class GameSerializer(serializers.Serializer):
    title = serializers.CharField()
    platforms = serializers.CharField()
    release_date = serializers.CharField()
    publisher = serializers.CharField()
    genres = serializers.CharField()
    editions = EditionSerializer(many=True)
