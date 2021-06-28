from django.db import models
from django import forms
from django.contrib import admin
# Create your models here.



class users(models.Model):

    name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 15)
    mobile = models.CharField(max_length = 12)
    password = models.CharField(max_length = 10)

    def __str__(self) -> str:
        return self.name


class password_for_users(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = users
        fields = "__all__"

class usersAdmin(admin.ModelAdmin):
    form = password_for_users