from django.db import models
class userInfo(models.Model):
    name= models.CharField(max_length=50)
    uname= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    age= models.IntegerField()

    def __str__(self):
        return self.uname

# Create your models here.
