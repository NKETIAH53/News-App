from django.contrib import admin
from .models import News, UserProfile


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(News, NewsAdmin)
admin.site.register(UserProfile)