from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    """Tweet Serializer using ModelSerializer for automatic field generation"""
    
    # User information
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    # Custom method field for like count
    like_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = [
            'id',
            'payload',
            'created_at',
            'updated_at',
            'user_id',
            'username',
            'like_count'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_like_count(self, obj):
        return obj.like_count()