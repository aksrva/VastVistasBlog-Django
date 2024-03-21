from configuration.models import Configuration, Navbar, SocialLinks
from datetime import datetime


def configurations(request):
    navbar_items = Navbar.objects.filter(is_active=True).order_by("priority")
    if request.user.is_authenticated:
        navbar_items = navbar_items.exclude(title="Register")
        navbar_items = navbar_items.exclude(title="Login")
    else:
        navbar_items = navbar_items.exclude(title="Logout")
    config = Configuration.objects.last()
    if not config:
        config = {
            "title": "<span>Vast</span><span>Vistas</span>",
            "is_search": True,
            "developer_links": "https://www.lapmos.com/",
            "developer_name": "Akash Kumar"
        }
    if not navbar_items:
        navbar_items = [{
            "title": "Home",
            "nav_link": "/"
        }]

    return {
        "configurations": config,
        "navbar": navbar_items,
        "social_links": SocialLinks.objects.filter(
            is_active=True).order_by("priority"),
        "current_year": datetime.now().year
    }
