
from south.db import db
from django.db import models
from blog.models import *

class Migration:
    
    def forwards(self):
        
        
        # Mock Models
        User = db.mock_model(model_name='User', db_table='auth_user', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'Entry'
        db.create_table('blog_entry', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(User)),
            ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ('status', models.IntegerField(choices=STATUS_CHOICES)),
            ('format', models.CharField(default='markdown', choices=FORMAT_CHOICES, max_length=25)),
            ('headline', models.CharField(max_length=250)),
            ('slug', models.SlugField()),
            ('summary', models.TextField(blank=True)),
            ('summary_html', models.TextField(blank=True)),
            ('body', models.TextField()),
            ('body_html', models.TextField(blank=True)),
            ('enable_comments', models.BooleanField(default=True)),
            ('tags', TagField()),
        ))
        
        db.send_create_signal('blog', ['Entry'])
    
    def backwards(self):
        db.delete_table('blog_entry')
        
