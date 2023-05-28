from django.db import models

# Create your models here.

class TaskModel(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']