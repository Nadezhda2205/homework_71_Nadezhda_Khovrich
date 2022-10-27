from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import LoginView, logout_view
from posts.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # path('signup/', SignupView.as_view(), name='signup'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
