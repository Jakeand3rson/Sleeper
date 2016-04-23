from django.db import models


class UserPresence(models.Model):
    """Associate a Slack user's presence with a timestamp."""

    timestamp = models.DateTimeField()
    slack_id = models.CharField(max_length=32)
    active = models.BooleanField()
