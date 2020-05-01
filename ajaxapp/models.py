from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    descriptions = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def only_date(self):
        return self.date.date()


class Comment(models.Model):
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text[:30]