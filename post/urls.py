from django.urls import path
from post.views import (
    # ConfigurationViewset,
    home, post, create_comment)
urlpatterns = [
    path('', home),
    path('create-comment/', create_comment),
    path('post/<str:slug>/', post),
    # path("api/config/", ConfigurationViewset.as_view({'get': 'list'})),
]
