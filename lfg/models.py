from django.conf import settings
from django.db import models


class LFG_Post(models.Model):
    title = models.CharField(max_length=60, unique=True)
    bio = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_players_needed = models.PositiveSmallIntegerField(
        null=False, blank=False, default=4
    )
    new_players_welcome = models.BooleanField()
    adult_content = models.BooleanField()
    paid_game = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "LFG"
        verbose_name_plural = "LFG List"
