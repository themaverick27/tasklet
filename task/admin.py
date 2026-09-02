from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list__title', 'created_at', 'updated_at')
    search_fields = ('title', 'list__title')
    list_filter = ('list__title', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    def __str__(self):
        return self.title

admin.site.register(Task, TaskAdmin)