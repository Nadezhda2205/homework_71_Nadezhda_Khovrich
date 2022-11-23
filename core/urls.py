from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import (
    LoginView, 
    logout_view, 
    RegisterView, 
    AccountDetailView, 
    unsubscribe_view, 
    subscribe_view,
    SearchAccountListView,
    SubscribersListView,
    SubscriptionsListView,
    AccountUpdateView
    )
from posts.views import (
    PostListView,
    PostCreateView,
    CommentCreateView,
    unlike_view,
    like_view,
    PostDetailView
    )


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    
    path('account/search', SearchAccountListView.as_view(), name='account_list'),
    path('<str:slug>/update', AccountUpdateView.as_view(), name='account_update'),
    
    path('<str:slug>/unsubscribe', unsubscribe_view, name='unsubscribe'),
    path('<str:slug>/subscribe', subscribe_view, name='subscribe'),
    path('<str:slug>', AccountDetailView.as_view(), name='account_detail'),

    path('<str:account>/subscribers', SubscribersListView.as_view(), name='subscribers'),
    path('<str:account>/subscriptions', SubscriptionsListView.as_view(), name='subscriptions'),


    path('post/<int:pk>/unlike', unlike_view, name='unlike'),
    path('post/<int:pk>/like', like_view, name='like'),

    path('post/add', PostCreateView.as_view(), name='post_add'),
    
    path('post/<int:pk>/comment/add', CommentCreateView.as_view(), name='post_comment_add'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
