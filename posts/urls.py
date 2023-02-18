from django.urls import path

from posts.views import home, create_post, save_post

app_name = "posts"

urlpatterns = [
    path("", home, name="index"),
    path("create", create_post, name="create"),
    path("save", save_post, name="save"),
]
