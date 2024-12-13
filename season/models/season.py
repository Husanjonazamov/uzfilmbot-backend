from django.db import models




class Season(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

