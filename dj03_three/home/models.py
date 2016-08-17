from django.db import models

# Create your models here.
class Profile(models.Model):
   name = models.CharField(max_length = 300)
   facebook= models.CharField(max_length = 500)
   class Meta:
      db_table = "profile"
