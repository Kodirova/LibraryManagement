from django.contrib import admin

from app.models import Book, Student, PurchasedBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    search_fields = ["full_name"]


@admin.register(PurchasedBook)
class PurchasedBookAdmin(admin.ModelAdmin):
    list_display = ['student', 'book']
    search_fields = ['student__full_name', 'book__name']

