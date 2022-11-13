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
    path("", terms_views.home, name="home"),
    path('add_term/', terms_views.add_term, name='add_term'),
    path('add_tag/', terms_views.add_tag, name="add_tag"),
    path('term_detail/<int:pk>', terms_views.term_detail, name="term_detail"),
    path('tag_detail/<int:pk>', terms_views.tag_detail, name="tag_detail"),
    path('term_library/', terms_views.term_library, name='term_library'),
    path('tag_list/', terms_views.tag_list, name='tag_list'),
    path('tags/<int:pk>', terms_views.tags, name='tags'),
    path("edit_term/<int:pk>/", terms_views.edit_term, name="edit_term"),
    path("edit_tag/<int:pk>/", terms_views.edit_tag, name="edit_tag"),
    path("delete_term/<int:pk>/", terms_views.delete_term, name="delete_term"),
    path("delete_tag/<int:pk>/", terms_views.delete_tag, name="delete_tag"),
    path("search/", terms_views.search_term.as_view(), name="search_results"),
    path("register", terms_views.register_request, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
   
]
