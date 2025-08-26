from django.contrib import admin
from .models import Tweet, Like


class ElonMuskFilter(admin.SimpleListFilter):
    """Custom filter for tweets mentioning Elon Musk"""

    title = "Elon Musk mentions"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return (
            ("contains", "Contains Elon Musk"),
            ("not_contains", "Does not contain Elon Musk"),
        )

    def queryset(self, request, queryset):
        if self.value() == "contains":
            return queryset.filter(payload__icontains="Elon Musk")
        elif self.value() == "not_contains":
            return queryset.exclude(payload__icontains="Elon Musk")
        return queryset


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payload",
        "like_count",
        "created_at",
    )
    search_fields = (
        "payload",
        "user__username",  # Search by username of user foreign key
    )
    list_filter = (
        "created_at",
        ElonMuskFilter,  # Custom filter for Elon Musk
        "user",
    )
    ordering = ("-created_at",)
    list_per_page = 20


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
        "created_at",
    )
    search_fields = ("user__username",)  # Search by username of user foreign key
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 20
