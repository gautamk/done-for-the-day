from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from googlelogin.models import GoogleUser


class GoogleUserAdmin(UserAdmin):
    pass


# Now register the new UserAdmin...
admin.site.register(GoogleUser, GoogleUserAdmin)
