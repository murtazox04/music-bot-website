from django.db import models
from django.contrib.auth.models import AbstractUser


class Audio(models.Model):
    title = models.CharField(max_length=255)
    message_id = models.IntegerField()
    from_user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'audio'

    def __str__(self):
        return self.title

# class User(AbstractUser):
#     telegram_id = models.IntegerField()
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['USERNAME']
#
#     def __str__(self):
#         return f"{self.username} - {self.telegram_id}"
