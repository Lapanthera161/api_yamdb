from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (Category, Comment, Genre,
                     Review, GenreTitle, Title, User)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'score',
        'pub_date',
        'title',
    )
    search_fields = ('title',)
    list_filter = (
        'author',
        'title',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'author',
        'pub_date',
        'review',
    )
    search_fields = ('review',)
    list_filter = (
        'review',
        'author',
    )


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
