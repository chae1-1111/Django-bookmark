from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)

# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')