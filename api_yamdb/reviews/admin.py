from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Genre, GenreTitle, Title, User

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
admin.site.register(User, UserAdmin)
