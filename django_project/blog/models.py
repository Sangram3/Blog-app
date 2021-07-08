from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# create real life objects here

class Post(models.Model):
    title = models.CharField(max_length = 60)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now   ) # date when post was posted but we can update the date if we want
    author = models.ForeignKey(User, on_delete = models.CASCADE) # when user is deleted all post get deleted
    # x = ForeignKey(y) => y can have many x's

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail' , kwargs = {'pk':self.pk})
