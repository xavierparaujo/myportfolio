from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("comment/<int:comment_id>", views.comment, name="comment"),
    path("new_post/", views.new_post, name="new_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
    path("delete_comment/<int:comment_id>/",
         views.delete_comment, name="delete_comment")
]
