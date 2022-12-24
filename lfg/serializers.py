from rest_framework import serializers

from lfg.models import LFG_Post


class LFGSerializer(serializers.ModelSerializer):
    class Meta:
        model = LFG_Post
        fields = (
            "title",
            "bio",
            "author",
            "total_players_needed",
            "new_players_welcome",
            "adult_content",
            "paid_game",
        )
