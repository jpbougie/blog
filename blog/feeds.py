from django.contrib.syndication.feeds import Feed
from models import Entry
import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

class LatestEntriesFeed(Feed):
    def title(self):
        return getattr(settings, 'BLOG_TITLE', 'Blog')
        
    def link(self):
        return 'http://' + Site.objects.get_current().domain + reverse('blog_entry_index')

    def description(self):
        return getattr(settings, 'BLOG_DESCRIPTION', '')
    
    def items(self):
        return Entry.published.filter(pub_date__lte=datetime.datetime.now())[:10]
        
    def item_pubdate(self, item):
        return item.pub_date