from django.contrib import admin
from .models import Post,UserProfile,Comment,Likes
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)