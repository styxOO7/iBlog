"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from home import views

from django.conf import settings
from django.conf.urls.static import static


from  django.conf import settings

# /* @import url(font-awesome.min.css); */


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('index', views.home, name='index'),
    path('generic/<id>', views.generic, name='generic'),
    path('confirmDelete/<id>', views.confirmDelete, name='confirmDelete'),
    path('deletePost/<id>', views.deletePost, name='deletePost'),
    path('updatePost/<id>', views.updatePost, name='updatePost'),
    path('updatePostHelp/<id>', views.updatePostHelp, name='updatePostHelp'),
    
    path('searchPage', views.searchPage, name='searchPage'),
    
    path('elements', views.elements, name='elements'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
