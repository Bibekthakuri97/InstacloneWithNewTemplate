from django.db import models
from user_app.models import UserModel

# Create your models here.
class Photomodel(models.Model):
    uploaded_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='uploaded_posts')
    time_stamp = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='upload_pic')
    caption = models.TextField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

        
class Commentmodel(models.Model):

    comment = models.TextField(max_length=200)
    timestamp1 = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    parent_post = models.ForeignKey(Photomodel,on_delete=models.CASCADE, related_name='comments')

