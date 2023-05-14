from django.contrib import admin
from .models import Author, Category, Subscriptions, Post, PostCategory,  Comment


# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Subscriptions)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)


#
