from django.contrib import admin
from .models import Topic, CrawledData

class CrawledDataInline(admin.StackedInline):
    model = CrawledData
    extra = 1

class CrawledDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


class TopicAdmin(admin.ModelAdmin):
    inlines = [CrawledDataInline]

admin.site.register(Topic, TopicAdmin)
admin.site.register(CrawledData, CrawledDataAdmin)