"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include 
from django.conf.urls.static import static
import debug_toolbar
from core import views as terms_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include ('debug_toolbar.urls')),
    path('add_term/', terms_views.add_term, name='add_term'),
    path('term_detail/<int:pk>', terms_views.term_detail, name="term_detail"),
    path('term_library/', terms_views.term_library, name='term_library'),
    path("edit_term/<int:pk>/", terms_views.edit_term, name="edit_term"),
    path("delete_term/<int:pk>/", terms_views.delete_term, name="delete_term"),
]
