from django.urls import path
from . import views

urlpatterns = [
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),  # Updated name for clarity
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),  # Correctly captures post_id
    path('blog/', views.blog_list, name='blog_list'),  # This is the list of all blog posts
    path('blog/<int:post_id>/comment/', views.add_comment, name='add_comment'),  # Capture post_id for comments
]
