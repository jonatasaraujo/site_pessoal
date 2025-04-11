from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/blog-detail/', views.blog_detail, name='blog_detail'),
]
