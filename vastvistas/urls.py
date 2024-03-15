from django.urls import path
from vastvistas.views import (
    ConfigurationViewset,
    home, post, create_comment, RegisterUser, login_view, logout_view)
urlpatterns = [
    path('', home),
    path('create-comment/', create_comment),
    path('post/<str:slug>/', post),
    path("api/config/", ConfigurationViewset.as_view({'get': 'list'})),
    # path('logout/', logout_view)
]
