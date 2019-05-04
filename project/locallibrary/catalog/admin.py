from django.contrib import admin

# Register your models here.

from catalog.models import Counselor, School, Student, Exam

admin.site.register(School)
admin.site.register(Exam)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    fields = ['first_name', 'last_name', 'phone_number']

admin.site.register(Counselor)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_school')