from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Tag
import markdown
#import markdown2
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.views.generic import ListView,DetailView
from django.db.models import Q
from pure_pagination import PaginationMixin

def search(request):
    
    q = request.GET.get('q')

    if not q:
        error_msg = "Please input search keywords"
        messages.add_message(request,messages.ERROR,error_msg,extra_tags='danger')
        return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q)|Q(body__icontains=q))
    return render(request,'blog/index.html',{'post_list':post_list})

class IndexView(PaginationMixin,ListView):
    model = Post
    template_name='blog/index.html'
    context_object_name='post_list'
    paginate_by=10
class ArchiveView(IndexView):
   # model = Post
   # template_name='blog/index.html'
   # context_object_name='post_list'
    def get_queryset(self):
        year=self.kwargs.get('year')
        month=self.kwargs.get('month')
        return super(ArchiveView,self).get_queryset().filter(create_time__year=year,create_time__month=month).order_by('-create_time')

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tag=t).order_by('-create_time')



class PostDetailView(DetailView):

    model = Post
    template_name ='blog/detail.html'
    context_object_name='post'

    def get(self,request,*args,**kwargs):
        response=super(PostDetailView,self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response

#    def get_object(value):

#        md = markdown.Markdown(extensions
#            =['markdown.extensions.extra','markdown.extensions.codehilite',TocExtension(slugify=slugify),])
#        content=md.convert(value)
#        m=re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#        toc=m.group(1) if m is not None else ''
#        return {"content":content,"toc":toc}
# Create your views here.
