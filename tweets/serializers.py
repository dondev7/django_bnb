from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.Serializer):
    """Tweet Serializer using base Serializer class (not ModelSerializer)"""
    
    id = serializers.IntegerField(read_only=True)
    payload = serializers.CharField(max_length=180)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    # User information
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    # Custom method field for like count
    like_count = serializers.SerializerMethodField()
    
    def get_like_count(self, obj):
        return obj.like_count()