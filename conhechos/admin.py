from django.contrib import admin
from conhechos.models import Eje, Descripcion, CumplimosLoPrometidoVideo, SliderVideo
import re
from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class ProjectAdminSite(AdminSite):
    login_template = "login.html"

class EjeAdmin(admin.ModelAdmin):
    pass

class DescripcionAdmin(admin.ModelAdmin):
    pass

class VideosCumplimosAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        link = form.cleaned_data.get("link")
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        validate = re.match(regex, link) is not None
        if validate == False:
            messages.add_message(request, messages.ERROR, 'Link no valido')
        else:
            super().save_model(request, obj, form, change)
            messages.add_message(request, messages.INFO, 'Se guardo correctamente')

class SliderVideoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        link = form.cleaned_data.get("link")
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        validate = re.match(regex, link) is not None
        if validate == False:
            messages.add_message(request, messages.ERROR, 'Link no valido')
        else:
            super().save_model(request, obj, form, change)
            messages.add_message(request, messages.INFO, 'Se guardo correctamente')

project_admin_site =  ProjectAdminSite(name='project_admin')        
project_admin_site.register(Eje, EjeAdmin)
project_admin_site.register(Descripcion, DescripcionAdmin)
project_admin_site.register(CumplimosLoPrometidoVideo, VideosCumplimosAdmin)
project_admin_site.register(SliderVideo, SliderVideoAdmin)
project_admin_site.register(User)
project_admin_site.register(Group)