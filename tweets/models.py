from django.db import models

class Tweet(models.Model):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        related_name="tweets",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payload[:50]  # Return first 50 characters of the tweet text
    
class Like(models.Model):
    tweet = models.ForeignKey(
        Tweet,
        related_name="likes",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        related_name="likes",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} likes {self.tweet.id}" 