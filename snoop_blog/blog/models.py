from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.CharField(max_length=500)
    pub_date=models.DateTimeField('fecha de publicacion')
    likes=models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    nombre=models.CharField(max_length=200)
    body=models.CharField(max_length=500)
    pub_date=models.DateTimeField('fecha de publicacion')
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
