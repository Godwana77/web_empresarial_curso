from django.contrib import admin

# Register your models here.
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
    

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-published',)
    list_display = ('title', 'author', 'published','post_category')
    ordering = ('author','-published',)
    search_fields = ('title','author__username','content')#important to use __ to access the related field)
    list_filter = ('author__username', 'published')
    date_hierarchy = 'published'
    
    def post_category(self, obj):
        return ", ".join([category.name for category in obj.category.all().order_by('name')])
    post_category.short_description = 'CATEGORIAS'
    
admin.site.register(Post, PostAdmin)
# admin.site.register(Post, PostAdmin)