from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import Issues
from .models import Moderators
from .models import Problems
from .models import Directions


admin.site.register(Directions)



class IssuesAdmin(admin.ModelAdmin):
    list_display = ('issue', 'status', 'pc_name', 'user_name', 'image_display', 'creation_time', 'closing_time')
    
    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'
    
    image_display.short_description = 'Изображение'
    
admin.site.register(Issues, IssuesAdmin)


class ModeratorsAdmin(admin.ModelAdmin):
    list_display = ('full_name', "month_tickets")
    
    
    
admin.site.register(Moderators, ModeratorsAdmin)




class ProblemsAdmin(admin.ModelAdmin):
    list_display = ('problem', 'parent')
    
    
admin.site.register(Problems, ProblemsAdmin)