from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic

class Status(models.Model):
    text    = models.TextField()
    author  = models.ForeignKey("auth.User")
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Statuses'
        ordering = ['created',]

class Plus(models.Model):
    user = models.ForeignKey(User)
    
    content_type = models.ForeignKey(ContentType, verbose_name='content type', blank=True, null=True)
    content_id = models.PositiveIntegerField(blank=True, null=True)
    content = generic.GenericForeignKey('content_type', 'content_id')

    class Meta:
        unique_together = ('user', 'content_type', 'content_id')
