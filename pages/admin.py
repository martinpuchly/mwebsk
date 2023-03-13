from django.contrib import admin
from .models import Page, Post, QuickNew, Tag

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
     exclude = ('views',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
     exclude = ('slug',)
     list_display = ('title', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
     fieldsets = [
          ('Článok', {'fields': ['title',  'tags', 'intro', 'body']}),
          ('SOE', {'fields': ['description', 'keywords']}),
          ('Publikovanie', {'fields': ['publised_at', 'publised']}),

     ]
     exclude = ('slug', 'views', 'likes', 'user')

     def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(QuickNew)
class QuickNewAdmin(admin.ModelAdmin):
    pass