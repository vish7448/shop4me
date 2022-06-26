from django.contrib import admin
from .models import deteail
@admin.register(deteail)

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'password')