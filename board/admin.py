from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'is_active')
    search_fields = ('name', 'owner__username')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


# Register your models here.
admin.site.register(Board, BoardAdmin)