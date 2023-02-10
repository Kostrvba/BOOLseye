from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='awatars')


class Post(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=200)
    likes = models.ManyToManyField(Profile, related_name='likes')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')
    saved = models.ManyToManyField(Profile, related_name="saved_post")


class Comments(models.Model):
    text = models.TextField(max_length=80)
    created = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post, related_name='post_comments')
