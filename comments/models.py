from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField('name',max_length=70)
    email = models.EmailField('email')
   # url = models.URLField('Web-site',blank=True)
    text = models.TextField()
    created_time = models.DateTimeField('created_time',default=timezone.now)
    post = models.ForeignKey('Blog.Post',on_delete=models.CASCADE)

    class Meta:
        verbose_name='comment'
        verbose_name_plural=verbose_name
        ordering = ['-created_time']

def __str__(self):
    return '{}:{}'.format(self.name,self.text[:20])

# Create your models here.
