from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('user/', include('users.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'),
         name="ck_editor_5_upload_file"),
    path("compiler/", include('compiler.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
