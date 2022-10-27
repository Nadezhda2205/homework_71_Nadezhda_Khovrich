from django.contrib import admin
from django.urls import path
from accounts.views import LoginView, logout_view
from posts.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # path('signup/', SignupView.as_view(), name='signup'),
]
