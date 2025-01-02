from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Adhar)
class Adhar(admin.ModelAdmin):
    list_display=['aadharNo','CreatedDate','createdBY']

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display=['Name','Email','contact','address','dob','adharno']

