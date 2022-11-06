from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from posts.models import Post, Comment
from posts.forms import CommentForm



class PostListView(ListView):
    template_name: str = 'posts/index.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context
        print(self.request.user.is_authenticated)
        user: Account = self.request.user
        subscriptions = user.subscriptions.all()
        posts = Post.objects.all()
        subscriptions_posts = posts.filter(author__in = subscriptions)
        context['posts'] = subscriptions_posts

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_add.html'
    model = Post
    fields = ['image', 'description']
    success_url = '/'

    def form_valid(self, form):
        self.object: Post = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
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


@login_required
def unlike_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    post_by_pk = get_object_or_404(Post, pk=pk)
    post_by_pk.liked_users.remove(user_from_request)
    if 'post' in request.META.get('HTTP_REFERER'):
        return redirect('post_detail', pk=pk)
    return redirect(f'/#{pk}')


@login_required
def like_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    post_by_pk = get_object_or_404(Post, pk=pk)
    post_by_pk.liked_users.add(user_from_request)
    if 'post' in request.META.get('HTTP_REFERER'):
        return redirect('post_detail', pk=pk)
    return redirect(f'/#{pk}')


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context
        