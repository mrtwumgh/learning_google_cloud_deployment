from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f"{self.user.username}'s Profile"