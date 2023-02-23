from django.contrib import admin
from .models import Seoul

class SeoulAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Seoul, SeoulAdmin)
