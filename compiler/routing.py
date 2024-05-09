from django.urls import path
from compiler.consumers import CodeExecutionConsumer

websocket_urlpatterns = [
    path('ws/code_execution/', CodeExecutionConsumer.as_asgi()),
]
