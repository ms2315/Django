from django.contrib import admin
from .models import Student, MyUser

# Register your models here.
@admin.register(MyUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'created_at', 'updated_at', 'created_by')