from django.contrib import admin
from .models import Term, User, Tag
from django.contrib.auth.admin import UserAdmin


admin.site.register(Term)
admin.site.register(User, UserAdmin)
admin.site.register(Tag, admin.ModelAdmin)
