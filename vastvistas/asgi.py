import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import compiler.routing as cr

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vastvistas.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            cr.websocket_urlpatterns
        )
    ),
})
