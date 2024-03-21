from django.db import models
from ckeditor.fields import RichTextField
from users.models import User


class PostCategory(models.Model):
    category = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    color = models.CharField(default="ff4c60", max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    STATUS = (
        (0, "DRAFT"),
        (1, "PUBLISH")
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextField(
        config_name='awesome_ckeditor', null=True, blank=True)
    meta_content = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to="static/post/images/",
                                  null=True, blank=True)
    compress_image = models.ImageField(upload_to="static/post/images/",
                                       null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image_border_color = models.CharField(max_length=6, default="ff4c60")
    time_to_read = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(default=0)
    category = models.ManyToManyField(PostCategory)
    status = models.IntegerField(choices=STATUS, default=0)
    is_active = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/post/images/",
                              null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title
