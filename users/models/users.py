from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
      return self.user_id
