from django.shortcuts import render,redirect
from blog.models import Post
from django.utils import timezone
from blog.forms import CommentForm
import logging
# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
  posts = (Post.objects
    .filter(published_at__lte=timezone.now())
    .order_by("-published_at")
    .select_related("author"))
  # log
  logger.debug(f'Got {len(posts)} posts')
  return render(request, "blog/index.html",{"posts": posts})

def post_detail(request,pk):
  post = Post.objects.get(pk=pk)
  
  if request.user.is_active:
    
    if request.method=="POST":
      comment_form = CommentForm(request.POST)
      
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        logger.info(f"comment created and saved on {post.pk} by {request.user}.")
        return redirect(request.path_info)
    else:
      comment_form = CommentForm
  else:
    comment_form = None
  
  return render(request,'blog/post-detail.html',{"post":post,"comment_form":comment_form})

