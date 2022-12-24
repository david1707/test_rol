from django.contrib import admin

from .models import LFG_Post


class LFGAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "total_players_needed",
        "new_players_welcome",
        "adult_content",
        "paid_game",
        "created_at",
    )
    fieldsets = (
        ("Summary", {"fields": ("title", "bio", "author")}),
        (
            "Options",
            {
                "fields": (
                    "total_players_needed",
                    "new_players_welcome",
                    "adult_content",
                    "paid_game",
                )
            },
        ),
    )


admin.site.register(LFG_Post, LFGAdmin)
