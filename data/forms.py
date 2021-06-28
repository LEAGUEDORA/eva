from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length= 20)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Password','required':'required'},))

class fileUpload(forms.Form):
    file_upload = forms.FileField()