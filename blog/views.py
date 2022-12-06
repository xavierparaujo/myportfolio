from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogComment
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse


# Home page
def home(response):
    posts = BlogPost.objects.order_by('-pub_date')
    return render(response, "blog/home.html", {'latest_posts': posts})


# Opens up a detail to a blog post
def detail(response, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if response.method == "POST":
        if response.POST.get("save_comment"):
            BlogComment(
                blog_post=post,
                comment_date=timezone.now(),
                username=response.POST.get("username"),
                comment=response.POST.get("comment")
            ).save()

    comments = BlogComment.objects.filter(blog_post__pk=post_id)

    return render(response, "blog/detail.html", {"post": post, "comments": comments})


def comment(response, comment_id):
    comment = get_object_or_404(BlogComment, pk=comment_id)
    return render(response, "blog/comment.html", {"comment": comment})


# Creates a new Blog Post
def new_post(response):
    if response.method == "POST":
        if response.POST.get("save_post"):
            BlogPost(title=response.POST.get("title"),
                     pub_date=timezone.now(),
                     text=response.POST.get("new_post")).save()
            return HttpResponseRedirect(reverse('blog:home'))

    return render(response, 'blog/post.html', {})


# Deletes a blog post
def delete_post(request, post_id):
    deletable = get_object_or_404(BlogPost, pk=post_id)
    deletable.delete()
    return HttpResponseRedirect(reverse('blog:home'))


# Deletes a comment
def delete_comment(request, comment_id):
    print("Hello World")
    deletable = get_object_or_404(BlogComment, pk=comment_id)
    post_id = deletable.blog_post.id
    deletable.delete()
    return HttpResponseRedirect(reverse("blog:detail", kwargs={'post_id': post_id}))
