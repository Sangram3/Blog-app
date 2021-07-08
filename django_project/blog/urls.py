from django.urls import path # importing path comand 
from . import views
from .views import ( PostListView, 
                     PostDetailView,
                     PostCreateView ,
                     PostUpdateView,
                     PostDeleteView,
                     UserPostListView)
# path : path(route, view , kwargs=None, name=None)

urlpatterns = [
    path('', PostListView.as_view(),name = 'blog-home'), # '' : home page , connect to views.home
    path('user/<str:username>', UserPostListView.as_view(),name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name = 'post-detail'), 
    path('post/new/', PostCreateView.as_view(),name = 'post-create'), 
    path('post/<int:pk>/update', PostUpdateView.as_view(),name = 'post-update'), 
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name = 'post-delete'), 
    
    path('about/', views.about, name = 'blog-about' ),
]