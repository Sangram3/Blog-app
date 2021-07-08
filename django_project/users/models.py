from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE) 
    # on deleting user Profile gets deleted
    # one user --> one profile 
    image = models.ImageField (default = 'default.jpg',upload_to = 'profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs): # over riding save method
        super().save(*args, **kwargs)
        # parent class's save method
        img = Image.open(self.image.path)
        if img.width > 400 or img.height > 400:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path )



