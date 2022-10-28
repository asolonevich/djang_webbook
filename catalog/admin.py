from atexit import register
from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language, Status

# Register your models here.
#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_birth', 'date_death']
    fields = ['first_name', 'last_name', ('date_birth', 'date_death')]
#Регистрация класса admin с соответствующей моделью
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'language', 'display_author']
    list_filter = ['genre', 'author']
    inlines = [BookInstanceInline]

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'borrower', 'due_back', 'id']
    list_filter = ['book', 'status', 'borrower']
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'name_print', 'inv_num')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back', 'borrower')})
    )
