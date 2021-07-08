from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
#importin class based views buitin
from django.views.generic import (ListView, 
                                 DetailView, 
                                 CreateView,
                                 UpdateView,
                                 DeleteView
                                 )
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


# def home(request):
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)


# List of all the posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name  = 'posts'
    ordering = '-date_posted'
    paginate_by = 5
# single post in detail
class PostDetailView(DetailView):
    model = Post


# List of all the posts by a single user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name  = 'posts'
    ordering = '-date_posted'
    paginate_by = 5

    # if user doesnt exist 404 returned
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

# single post in detail
class PostDetailView(DetailView):
    model = Post

#creating new post
#login required to create post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    # over riding form_view method
    def form_valid(self,form):
        form.instance.author = self.request.user
        # set the author of the post that has been created 
        return super().form_valid(form)

#login required & user should be author of the post
class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        # set the author of the post that has been created 
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # redirect to home page after deleting the post
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False



def about(request):
    return render(request,'blog/about.html',{'title' : 'About'})