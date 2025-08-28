from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    
    # API endpoints
    path('api/v1/tweets', api_views.TweetListView.as_view(), name='api_tweet_list'),
    path('api/v1/users/<int:user_id>/tweets', api_views.UserTweetsView.as_view(), name='api_user_tweets'),
]