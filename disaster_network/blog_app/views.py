from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    return render(request, 'blog/blog_details.html', {'post': post, 'comments': comments})


@login_required
def add_blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Check if the title and content fields are provided
        if not title or not content:
            error_message = "Title and content are required."
            return render(request, 'blog/add_blog_post.html', {'error': error_message})

        # Create a new BlogPost instance and save it
        blog_post = BlogPost.objects.create(
            title=title,
            content=content,
            author=request.user
        )

        # Redirect to the blog list view after successful creation
        return redirect('blog_list')

    # Render the add_blog_post.html template
    return render(request, 'blog/add_blog_post.html')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        
        if not content:
            error_message = "Comment content is required."
            return render(request,'blog/add_comment.html',{'error':error_message,'post':post})
        
        comment = Comment.objects.create(
            blog_post=post,
            content=content,
            author=request.user
        )
        
        return redirect('blog_detail',post_id=post.id)
    return render(request,'blog/add_comment.html',{'post':post})


        