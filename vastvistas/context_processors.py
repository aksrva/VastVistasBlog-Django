from vastvistas.models import Configuration, Navbar, SocialLinks
from datetime import datetime


def configurations(request):
    navbar_items = Navbar.objects.filter(is_active=True).order_by("priority")
    if request.user.is_authenticated:
        navbar_items = navbar_items.exclude(title="Register")
        navbar_items = navbar_items.exclude(title="Login")
    else:
        navbar_items = navbar_items.exclude(title="Logout")
    return {
        "configurations": Configuration.objects.last(),
        "navbar": navbar_items,
        "social_links": SocialLinks.objects.filter(
            is_active=True).order_by("priority"),
        "current_year": datetime.now().year
    }
