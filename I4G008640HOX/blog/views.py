from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView   
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

    # PostCreateview
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

    # PostDetailview
class PostDetailView(DetailView):
    model = Post

    # PostUpdateview
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    # Postdeleteview
class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")