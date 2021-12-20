from movie_app.serializers import MovieSerializer
from django.contrib import admin
from .models import Movie

# Register your models here.
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status', 'author', 'created_on')
#     list_filter = ('author',)
#     search_fields = ('title', 'content'),
#     prepopulated_fields = ({'slug': ('title',)})

# admin.site.register(Blog, BlogAdmin)
admin.site.register(Movie)
