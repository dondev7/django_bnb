from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tweet
from .serializers import TweetSerializer
from users.models import User


class TweetListView(APIView):
    """
    API endpoint to show all tweets
    URL: /api/v1/tweets
    """
    
    def get(self, request):
        """Handle GET request to retrieve all tweets"""
        tweets = Tweet.objects.all().select_related('user').order_by('-created_at')
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserTweetsView(APIView):
    """
    API endpoint to show all tweets by a specific user
    URL: /api/v1/users/<user_id>/tweets
    Handles User.DoesNotExist exception
    """
    
    def get(self, request, user_id):
        """Handle GET request to retrieve tweets by specific user"""
        # This will raise 404 if user doesn't exist
        user = get_object_or_404(User, id=user_id)
        tweets = Tweet.objects.filter(user=user).select_related('user').order_by('-created_at')
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)