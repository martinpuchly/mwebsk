from django.shortcuts import render
from .models import Page, Post
from django.shortcuts import get_object_or_404, render


def page_show(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    return render(request, "pages/show.html", {
        'page': page
    })


def post_index(request):
    posts = Post.objects.order_by('-created_at').all()[:5]
    return render(request, "posts/index.html", {
        'posts': posts
    })

def post_tag_index(request, tag):
    posts = Post.objects.filter(tags__slug=tag).all()[:5]
    return render(request, "posts/index.html", {
        'posts': posts
    })

def post_show(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    #VIEWS COUNT +1
    if request.session.get(f"post_view_{post.id}")==False:
        post.views+=1
        post.save()
        request.session[f"post_view_{post.id}"] = True
        
    return render(request, "posts/show.html", {
        'post': post
    })