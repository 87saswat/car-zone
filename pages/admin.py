from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    # displays photos in admin
    def thumbnail(self, object):
        return format_html('<img src="{}" width=40 style="border-radius: 50px;"/>'.format(object.photo.url))
    
    # change the builtin "Thumbnail" name toour customized name
    thumbnail.short_description = "Photo"

    list_display = ('id', 'thumbnail','first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail','first_name','designation')                                       #for the text to be clickable link
    search_fields = ('first_name', 'last_name',)
    list_filter = ('designation',)




admin.site.register(Team, TeamAdmin)
 