from django.contrib import admin
from .models import BlogComment, BlogPost

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogComment)
