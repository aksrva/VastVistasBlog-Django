from django.db import models


class SocialLinks(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    icon_image = models.ImageField(upload_to="static/social_icons/",
                                   null=True, blank=True)
    html_icon = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Linkss"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.title


class Navbar(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    nav_link = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Configuration(models.Model):
    title = models.CharField(max_length=255, default="Vast",
                             null=True, blank=True)
    title2 = models.CharField(max_length=255, default="Vistas",
                              null=True, blank=True)
    meta_title = models.CharField(max_length=255, default="VastVistas",
                                  null=True, blank=True)
    post_count = models.IntegerField(default=12)
    is_search = models.BooleanField(default=True)
    developer_name = models.CharField(max_length=255, default="Akash Kumar")
    developer_links = models.CharField(max_length=255,
                                       default="https://www.lapmos.com/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meta_title
