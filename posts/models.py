from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    updated_at = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.title