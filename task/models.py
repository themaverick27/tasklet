from django.db import models
from list.models import List

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    due_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(
        List,
        on_delete = models.CASCADE,
        related_name='tasks'
    )

    def __str__(self):
        return self.title