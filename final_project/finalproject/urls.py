from django.contrib import admin
from django.urls import path 
from final_project import urls as finalproject_url
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(finalproject_url, namespace='finalproject'))
]