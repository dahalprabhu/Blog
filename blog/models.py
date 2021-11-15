from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " by " + self.author

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=15)
    email= models.CharField(max_length=50)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return "Message from " + self.name + ' - ' + self.email