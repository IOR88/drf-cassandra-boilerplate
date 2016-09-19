from django.contrib import admin

from .models import CassandraAdventuresModel


# Register your models here.
class CassandraAdventuresAdmin(admin.ModelAdmin):
    list_display = (
        'adventure_id', 'adventure_desc' , 'last_modified'
    )
admin.site.register(CassandraAdventuresModel, CassandraAdventuresAdmin)    