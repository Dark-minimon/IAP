from django.contrib import admin
from newIAPapp.models import Mission
# Register your models here.
# admin.site.register([Mission])


class MissionAdmin(admin.ModelAdmin):
    list_editable = ['title', 'descr', 'sphere', 'imp', 'deadline', 'user']
    fields = ['title', 'descr', 'sphere', 'imp', 'deadline', 'user']
    search_fields = ['title', 'descr', 'sphere', 'imp', 'deadline', 'user']
    list_filter = ['title', 'descr', 'sphere', 'imp', 'deadline', 'user']
    list_display_links = ['edit']
    list_display = ['title', 'descr', 'sphere', 'imp', 'deadline', 'user', 'edit']


admin.site.register(Mission, MissionAdmin)
