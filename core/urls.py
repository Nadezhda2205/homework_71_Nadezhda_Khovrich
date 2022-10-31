from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import (
    LoginView, 
    logout_view, 
    RegisterView, 
    AccountDetailView, 
    unsubscribe_view, 
    subscribe_view,
    SearchAccountListView
)
from posts.views import PostListView, PostCreateView, CommentCreateView, unlike_view, like_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    
    path('account/search', SearchAccountListView.as_view(), name='account_list'),
    path('account/<str:slug>', AccountDetailView.as_view(), name='account_detail'),
    
    
    path('unsubscribe/<str:slug>', unsubscribe_view, name='unsubscribe'),
    path('subscribe/<str:slug>', subscribe_view, name='subscribe'),


    path('post/<int:pk>/unlike', unlike_view, name='unlike'),
    path('post/<int:pk>/like', like_view, name='like'),

    path('post/add', PostCreateView.as_view(), name='post_add'),
    
    path('post/<int:pk>/comment/add', CommentCreateView.as_view(), name='post_comment_add'),
    




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
