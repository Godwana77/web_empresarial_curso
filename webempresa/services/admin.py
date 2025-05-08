from django.contrib import admin

# Register your models here.
from .models import Store

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    

admin.site.register(Store, ServiceAdmin)