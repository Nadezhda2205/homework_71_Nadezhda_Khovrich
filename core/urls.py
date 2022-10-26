from django.contrib import admin
from django.urls import path
from accounts.views import LoginView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # path('signup/', SignupView.as_view(), name='signup'),
]
