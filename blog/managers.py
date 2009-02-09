from django.db import models

class PublishedManager(models.Manager):
    """
        This manager filters the entry based on the published status
    """
    
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(status__exact=self.model.PUBLISHED_STATUS)