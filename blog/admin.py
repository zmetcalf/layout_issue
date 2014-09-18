from django.contrib import admin

from widgy_blog.admin import BlogAdmin
from widgy_blog.models import Blog

from blog.models import News


class NewsAdmin(BlogAdmin):
    layout_proxy_fields = [
        'title',
        'slug',
        'date',
        'summary',
        'description',
        'keywords',
        'page_title',
    ]
    list_display = ['title']
    fieldsets = [
        (None, {
            'fields': [
                'title', 'date', 'summary', 'content',
            ],
        }),
        ('Meta', {
            'fields': ['description', 'keywords', 'slug', 'page_title'],
            'classes': ['collapse', 'grp-collapse', 'collapse-closed',
                        'collapsed'],
        }),
    ]

admin.site.unregister(Blog)
admin.site.register(News, NewsAdmin)
