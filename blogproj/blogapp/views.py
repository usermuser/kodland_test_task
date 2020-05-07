from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.shortcuts import redirect

from .models import Post


def redirect_to_posts(request):
    return redirect('blogapp:posts', permanent=True)


class PostsView(generic.ListView):
    template_name = 'blogapp/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-created')[:10]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogapp/detail.html'


class PostCreate(CreateView):
    model = Post
    fields = '__all__'


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp:posts')
