from django.shortcuts import redirect, get_object_or_404
from posts.models import Post, Comment
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse
from posts.forms import CommentForm
from django.core.handlers.wsgi import WSGIRequest
from accounts.models import Account



class PostListView(ListView):
    template_name: str = 'posts/index.html'
    model = Post
    context_object_name = 'posts'


class PostCreateView(CreateView):
    template_name = 'posts/post_add.html'
    model = Post
    fields = ['image', 'description']
    success_url = '/'

    def form_valid(self, form):
        self.object: Post = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = '/'

    def form_valid(self, form):
        self.object: Comment = form.save(commit=False)
        post_pk = self.kwargs.get('pk')
        self.object.post = get_object_or_404(Post, pk=post_pk)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs.get('pk')})


def unlike_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    post_by_pk = get_object_or_404(Post, pk=pk)
    post_by_pk.liked_users.remove(user_from_request)
    return redirect ('index')


def like_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    post_by_pk = get_object_or_404(Post, pk=pk)
    post_by_pk.liked_users.add(user_from_request)
    return redirect ('index')


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context