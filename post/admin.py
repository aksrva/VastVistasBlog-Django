from django.contrib import admin
from post.models import PostCategory, Post, PostComment
import math
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.safestring import mark_safe


def compress_image(uploadedImage):
    imageTemproary = Image.open(uploadedImage)
    outputIoStream = BytesIO()
    imageTemproary.save(outputIoStream, format='JPEG', quality=10)
    outputIoStream.seek(0)
    new_file_name = "%s_compressed.jpg" % uploadedImage.name.split('.')[0]
    uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField',
                                         new_file_name, 'image/jpeg',
                                         sys.getsizeof(outputIoStream), None)
    return uploadedImage


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "time_to_read")

    def formatted_content(self, obj):
        return mark_safe(obj.content)
    formatted_content.short_description = "Content"

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super().get_readonly_fields(request, obj)
        if obj and obj.author != request.user:
            read_only_fields += ('title', 'slug', 'formatted_content',
                                 'thumbnail', 'image_border_color', 'views',
                                 'category', 'priority', 'compress_image',
                                 'meta_content')
            self.exclude = ('content',)
        if not request.user.is_superuser:
            read_only_fields += (
                'priority', 'is_approved', 'status', 'is_active', 'author',
                'time_to_read')
        if 'title' not in read_only_fields and 'slug' not in read_only_fields:
            self.prepopulated_fields = {"slug": ("title",)}
        if request.user.is_superuser:
            self.exclude = ()
            read_only_fields = ()
        return read_only_fields

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user

        words = obj.content.split()
        num_words = len(words)
        reading_time_minutes = num_words / 200
        obj.time_to_read = math.ceil(reading_time_minutes)
        obj.compress_image = compress_image(obj.thumbnail)
        super().save_model(request, obj, form, change)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at", "updated_at")


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "is_active", "priority",
                    "color", "created_at", "updated_at")


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
