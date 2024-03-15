from django.urls import path
from vastvistas.views import RegisterUser, login_view, logout_view
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', login_view),
    path('logout/', logout_view)
]
