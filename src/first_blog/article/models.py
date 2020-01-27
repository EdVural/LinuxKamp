from django.db import models
from django.contrib.auth.admin import User
# Create your models here.
from django.db.models import TextField


class Post(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    draft = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    liked = models.IntegerField(default=0)
    comment = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='articles')
    title = models.TextField()

    def __str__(self):
        return self.header


class Comment(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Reply to {self.header}"
