from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vastvistas_web.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('user/', include('user.urls')),
]
