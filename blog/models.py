from django.db import models


class BlogPost(models.Model):
    pub_date = models.DateTimeField("published date")
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_date = models.DateTimeField("comment date")
    username = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.comment
