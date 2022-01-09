from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    #list_display: Controls which fields appear on the managed change list page
    #fields:  Make simple layout changes in the forms on the Add add Change pages
    list_display=['name','url','email','created_time','post']
    fields = ['name','email','url','text','post']

admin.site.register(Comment,CommentAdmin)


# Register your models here.
