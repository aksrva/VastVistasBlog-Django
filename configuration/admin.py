from django.contrib import admin

from configuration.models import Configuration, Navbar, SocialLinks


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_image", "html_icon", "is_active",
                    "priority", "created_at", "updated_at")


class NavbarAdmin(admin.ModelAdmin):
    list_display = ("title", "nav_link", "is_active", "priority",
                    "created_at", "updated_at")
    actions = ["active_deactive_navbar"]

    def active_deactive_navbar(self, request, queryset):
        for row in queryset:
            row.is_active = not row.is_active
            row.save()


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "meta_title")


admin.site.register(SocialLinks, SocialLinksAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
