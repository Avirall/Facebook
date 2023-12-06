from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=2000,null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True,default=0)
    media_file = models.FileField(upload_to='media/',null=True,blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created=models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=3000)

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
