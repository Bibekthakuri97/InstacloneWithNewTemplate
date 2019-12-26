from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=20, unique=True)
    passwrod = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255,blank=True)
    photo = models.ImageField(upload_to='profile_pic')
    followers = models.ManyToManyField('UserModel', related_name='followings',symmetrical=False,blank=True)

    def __str__(self):
        return self.username