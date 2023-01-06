from django.contrib import admin
from blog_app.models import Comment, Post, Category, Tag, NewsLetter, Contact

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(NewsLetter)
admin.site.register(Contact)
admin.site.register(Comment)
