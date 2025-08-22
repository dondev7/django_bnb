from django.contrib import admin
from .models import Tweet, Like

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'payload', 'created_at', 'updated_at')
    search_fields = ('payload',)
    list_filter = ('user', 'created_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'created_at', 'updated_at')
    search_fields = ('user__username', 'tweet__payload')
    list_filter = ('user', 'tweet', 'created_at')



