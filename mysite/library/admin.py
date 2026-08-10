from django.contrib import admin
from .models import Genre, Author, Book, BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'display_genre', 'author']

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'status', 'due_back']

# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
