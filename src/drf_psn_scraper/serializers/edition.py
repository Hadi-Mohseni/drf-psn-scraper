from rest_framework import serializers


class EditionSerializer(serializers.Serializer):
    title = serializers.CharField()
    original_price = serializers.CharField()
    discount_price = serializers.CharField()
    currency = serializers.CharField()
