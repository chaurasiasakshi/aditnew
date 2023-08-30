from django.contrib import admin

# Register your models here.

from .models import promodel

@admin.register(promodel)

class proAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','subject','message')