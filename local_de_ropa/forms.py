from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import  User
from django.forms import PasswordInput


class form_remeras(forms.Form):

    modelo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    stock = forms.IntegerField()
   
   
class form_buzos(forms.Form):

    modelo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    stock = forms.IntegerField()  


class form_jeans(forms.Form):

    modelo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    stock = forms.IntegerField()  



class form_camperas(forms.Form):

    modelo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    stock = forms.IntegerField()  








class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña",widget=forms.PasswordInput, max_length=30)
    password2 = forms.CharField(label="repetir contraseña",widget=forms.PasswordInput, max_length=30)

    


class ChancePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "old password"}))
    new_password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "new password"}))
    new_password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "confirm new password"}))

    class meta:
        
        model = User
        fields = ["old_password","new_password1","new_password1"]
        help_texts ={k:"" for k in fields}



class Avatarformulario(forms.Form):
    avatar = forms.ImageField()