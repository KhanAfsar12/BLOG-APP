from django.contrib import admin

from .models import Category, Post

# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description','url', 'image',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = (
            'https://cdn.tiny.cloud/1/your_api_key_here/tinymce/5/tinymce.min.js',  # Replace with your actual API key
            'js/init_tinymce.js',
        )
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
