from django.contrib.syndication.feeds import Feed
from models import Entry
import datetime

class BlogEntryFeed(Feed):
    title = "jpbougie.net - blog"
    link = "http://www.jpbougie.net/blog/"
    description = "Adventures in Italy"
    
    def items(self):
        return Entry.published.filter(pub_date__lte=datetime.datetime.now())[:10]
        
    def item_pubdate(self, item):
        return item.pub_date