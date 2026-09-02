from django.contrib import admin
from .models import List

class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'board__name', 'created_at')
    search_fields = ('title', 'board__name')
    list_filter = ('board__name',)
    ordering = ('-created_at',)


# Register your models here.
admin.site.register(List, ListAdmin)