from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    """Tweet Model Definition"""

    payload = models.CharField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return self.payload[:50]  # Return first 50 characters of the tweet text

    def like_count(self):
        return self.likes.count()


class Like(CommonModel):
    """Like Model Definition"""

    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.tweet.payload}"
