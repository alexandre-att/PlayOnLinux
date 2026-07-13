"""PlayOnLinux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import (handler400, handler403, handler404, handler500)
from PlayOnLinux import views

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path('version2.php', views.version2),
    path('update_mark.txt', views.update_mark),
    path('V4_data/repository/screenshot.php', views.screenshot),
    path('V4_data/repository/get_packages.php', views.get_packages),
    path('V4_data/repository/get_description.php', views.get_description),
    path('V4_data/repository/stars.php', views.stars),
    path('V4_data/repository/get_file.php', views.get_file),
    path('V4_data/repository/get_list_v4.php', views.get_list_v4),
    path('V4_data/repository/get_md5_list.php', views.get_md5_list),
    path('download/<str:filename>', views.download),
]

handler404 = 'PlayOnLinux.views.custom_page_not_found_view'
handler500 = 'PlayOnLinux.views.custom_error_view'
handler403 = 'PlayOnLinux.views.custom_permission_denied_view'
handler400 = 'PlayOnLinux.views.custom_bad_request_view'
