# tasks/models.py
from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=1, default='M', choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
