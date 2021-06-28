from django.contrib import admin
from . models import users, password_for_users, usersAdmin
# Register your models here.


admin.site.register(users, usersAdmin)