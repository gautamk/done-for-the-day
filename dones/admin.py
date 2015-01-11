from django.contrib import admin

# Register your models here.
from dones.models import Done


class DoneAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_done', 'created_by', 'created_at', 'modified_at')
    list_filter = ('is_done', 'created_by', 'created_at')


admin.site.register(Done, DoneAdmin)