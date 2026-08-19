from django.contrib import admin
from .models import Genre, Author, Book, BookInstance, BookReview

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'display_books']
    readonly_fields = ['display_books']

    fieldsets = [
        ('General', {'fields': ('first_name', 'last_name', 'description', 'display_books')}),
    ]

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0
    readonly_fields = ['uuid']
    fields = ['uuid', 'due_back', 'status']
    can_delete = False

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'display_genre', 'author']
    inlines = [BookInstanceInLine]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'book', 'status', 'reader', 'due_back', 'is_overdue']
    list_filter = ['book', 'status', 'due_back']
    list_editable = ['status', 'reader', 'due_back']
    search_fields = ['uuid', 'book__title',
                     'book__author__first_name',
                     'book__author__last_name']

    fieldsets = [
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'reader', 'due_back')}),
    ]

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'author', 'date', 'content']



# Register your models here.
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(BookReview, BookReviewAdmin)
