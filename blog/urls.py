from django.conf.urls.defaults import *
from django.views.generic import date_based

from models import Entry
from feeds import LatestEntriesFeed

entry_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('',
    url(r'^$', date_based.archive_index, entry_dict, name='blog_entry_index'),
    url(r'^(?P<year>\d{4})/$', date_based.archive_year, entry_dict, name='blog_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', date_based.archive_month, entry_dict, name='blog_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', date_based.archive_day, entry_dict, name='blog_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', date_based.object_detail, dict(entry_dict, slug_field='slug'), name='blog_entry_detail'),
    )
    
urlpatterns += patterns('', 
    (r'^comments/', include('django.contrib.comments.urls')))

feeds = {
    'latest': LatestEntriesFeed,
}

urlpatterns += patterns('',
   url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
   )
