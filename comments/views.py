from django.shortcuts import render,get_object_or_404,redirect
from Blog.models import Post
from .models import Comment
from users.models import User
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.contrib import messages
@require_POST
def comment(request,post_pk):

    post = get_object_or_404(Post,pk=post_pk)
  #  email = comments.object.get(name=name).email
 #   form = CommentForm(request.POST)
 #   name = request.POST.get('username')
  #  print(name)
    form = CommentForm(request.POST)

#    email = Comment.objects.get(name=name).email
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
      #  comment.name=name
        comment.save()

        messages.add_message(request,messages.SUCCESS,'Submit success!',extra_tags='success')
        return redirect(post)

    context={'post':post,
             'form':form,
             }
    messages.add_message(request,messages.ERROR,'Submit failed!',extra_tags='failed')
    return render(request,'comments/preview.html',context=context)

# Create your views here.
