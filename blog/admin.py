from django.contrib import admin
from blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("headline",)}
    exclude = ('summary_html', 'body_html')
    date_hierarchy = 'pub_date'

admin.site.register(Entry, EntryAdmin)