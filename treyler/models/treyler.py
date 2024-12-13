from django.db import models



class Treyler(models.Model):
  title = models.CharField(max_length=25)
  treyler_id = models.CharField(max_length=250)
  description = models.TextField()
  code = models.CharField(max_length=10)


  def __str__(self) -> str:
    return self.title
