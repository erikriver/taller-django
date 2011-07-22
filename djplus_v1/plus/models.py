from django.db import models

class Status(models.Model):
    text    = models.TextField()
    author  = models.ForeignKey("auth.User")
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Statuses'
        ordering = ['created',]
        
