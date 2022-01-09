from django import template
from . .models import Post, Category, Tag
from  django.db.models.aggregates import Count
register = template.Library()

@register.inclusion_tag('blog/inclusions/_recent_post.html',takes_context=True)
def show_recent_post(context,num=5):
    return{
            'recent_post_list':Post.objects.all().order_by('-create_time')[:num],
            }

@register.inclusion_tag('blog/inclusions/_archives.html',takes_context=True)
def show_archives(context):
    return{
            'date_list':Post.objects.dates('create_time','month',order='DESC'),
            }

@register.inclusion_tag('blog/inclusions/_categories.html',takes_context=True)
def show_categories(context):
    category_list=Category.objects.annotate(nums_posts=Count('post')).filter(nums_posts__gt=0)
    return{
        'category_list':Category.objects.all(),
            }

@register.inclusion_tag('blog/inclusions/_tags.html',takes_context=True)
def show_tags(context):
    tag_list=Tag.objects.annotate(nums_posts=Count('post')).filter(nums_posts__gt=0)
    return{
        'tag_list':Tag.objects.all(),
            }
