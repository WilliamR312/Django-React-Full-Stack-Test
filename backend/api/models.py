from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # Don't passing this, automaticaly populate it with now
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") # Link with other table  / deleted when user removed / link data with user

    def __str__(self):
        return self.title