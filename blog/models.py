from django.db import models
from django.urls import reverse
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    body = models.TextField()
    topic = models.CharField(max_length=50)
    publication = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
