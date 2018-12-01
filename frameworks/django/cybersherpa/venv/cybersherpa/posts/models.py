from django.db import models

# Create your models here.
class Post(models.Model):

    #title
    title = models.CharField(max_length=250)
    #date
    pub_date = models.DateTimeField()
    #Image
    image = models.ImageField(upload_to='media/')
    #text
    body = models.TextField()
