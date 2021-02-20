from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('', home, name='home'),
]
