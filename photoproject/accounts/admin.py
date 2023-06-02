from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
# Register your models here.

    list_display = ('id','username')

    list_display_links = ('id','username')

admin.site.register(CustomUser, CustomUserAdmin)