from django.urls import path
from vastvistas_web.views import RegisterUser, login_view, logout_view
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', login_view),
    path('logout/', logout_view)
]
