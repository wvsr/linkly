from django.db import models

# Create your models here.
class UrlModel(models.Model):
 main_url = models.CharField(max_length=1200)
 short_url = models.CharField(max_length=100)
 date = models.DateField(auto_now_add=True)