from django.db import models

# Create your models here.
class UrlModel(models.Model):
 main_url = models.CharField(max_length=1200) #user submit url
 short_url = models.CharField(max_length=100) #created short url
 serve_count = models.IntegerField(default=0) # count serving
 date = models.DateField(auto_now_add=True)