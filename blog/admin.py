from django.contrib import admin
from blog.models import Post , Category ,Comments






#Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title','is_active']
    


@admin.register(Category)
class CategoryAdmim(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
   list_display = ['pk','posts','comments_author','comment_content','comment_date']








# admin.site.register(Blog)
