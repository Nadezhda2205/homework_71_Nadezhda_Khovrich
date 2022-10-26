from django import forms



class LoginForm(forms.Form):
    '''форма для входа'''
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)

