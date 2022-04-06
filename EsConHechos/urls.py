"""EsConHechos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from conhechos.views import home, interna, handler404, handler403, handler500
from django.conf import settings
from django.conf.urls.static import static
from conhechos.admin import project_admin_site
urlpatterns = [
    path('admin/', project_admin_site.urls),
    path('',home),
    path('eje/<str:eje>',interna),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404
handler500 = handler500
handler403 = handler403
