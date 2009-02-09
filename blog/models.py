from django.db import models
from django.contrib.auth.models import User

import datetime
import tagging
from tagging.fields import TagField
from template_utils.markup import formatter

try:
    from typogrify.templatetags.typogrify import typogrify
except ImportError:
    typogrify = None
    
from blog import managers

class Entry(models.Model):
    """
        A single entry in the blog
    """
    
    PUBLISHED_STATUS = 1
    DRAFT_STATUS = 2
    
    STATUS_CHOICES = (
        (PUBLISHED_STATUS, 'Published'),
        (DRAFT_STATUS, 'Draft'),
    )
    
    FORMAT_CHOICES = ((key, key) for key in formatter._filters.keys())
    
    author = models.ForeignKey(User)
    
    pub_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    status = models.IntegerField(choices=STATUS_CHOICES)
    
    format = models.CharField(default='markdown', choices=FORMAT_CHOICES, max_length=25)
    
    headline = models.CharField(max_length=250)
    slug = models.SlugField()
    
    summary = models.TextField(blank=True)
    summary_html = models.TextField(blank=True)
    
    body = models.TextField()
    body_html = models.TextField(blank=True)
    
    enable_comments = models.BooleanField(default=True)
    
    tags = TagField()
    
    published = managers.PublishedManager()
    objects = models.Manager()
    
    class Meta:
        get_latest_by = 'pub_date'
        verbose_name_plural = 'Entries'

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry_detail', (), {
                'year': self.pub_date.year,
                'month': self.pub_date.strftime("%b").lower(),
                'day': self.pub_date.day,
                'slug': self.slug })
                
    def save(self, force_insert=False, force_update=False):
        if self.summary:
            self.summary_html = formatter(self.summary, filter_name=self.format)
            if typogrify:
                self.summary_html = typogrify(self.summary_html)
  
        self.body_html = formatter(self.body, filter_name=self.format)
        if typogrify:
            self.body_html = typogrify(self.body_html)
        super(Entry, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.headline