from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tweet
from .serializers import TweetSerializer
from users.models import User


class TweetListView(generics.ListAPIView):
    """
    API endpoint to show all tweets
    URL: /api/v1/tweets
    """
    queryset = Tweet.objects.all().select_related('user').order_by('-created_at')
    serializer_class = TweetSerializer


class UserTweetsView(generics.ListAPIView):
    """
    API endpoint to show all tweets by a specific user
    URL: /api/v1/users/<user_id>/tweets
    Handles User.DoesNotExist exception
    """
    serializer_class = TweetSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        # This will raise 404 if user doesn't exist
        user = get_object_or_404(User, id=user_id)
        return Tweet.objects.filter(user=user).select_related('user').order_by('-created_at')