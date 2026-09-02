from django.db import models
from board.models import Board

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(
        Board,
        on_delete = models.CASCADE,
        related_name='lists'
    )

    def __str__(self):
        return self.title