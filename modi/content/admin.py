from django.contrib import admin
from .models import shoes_mo, mobile, baby_mo, footwear_mo
# Register your models here.
@admin.register(shoes_mo, baby_mo, footwear_mo, mobile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'disc', 'price', 'product_image')
