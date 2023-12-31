﻿from django import forms
from django.db import models
from .models import Comment, Phone
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Blog

class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", min_length = 2, max_length = 100)
    city = forms.CharField(label="Ваш город", min_length = 2, max_length = 100, required=False)
    job = forms.CharField(label="Ваша профессия или род занятий", min_length = 2, max_length = 100)
    gender = forms.ChoiceField(label="Ваш пол", 
                               choices=[('1', 'Мужской'), ('2','Женский')], 
                               widget=forms.RadioSelect)
    notice = forms.BooleanField(label="Получать новости сайта на e-mail?", required=False)    
    email = forms.CharField(label="Ваш e-mail",min_length=7)
    message = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'rows':8, 'cols':40}))
    
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
    
class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
        
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','description','content','image')
        labels={'title':'Заголовок','description':'Краткое содержание','content':'Полное содержание','image':'Картинка'}
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Phone
        fields=('title','description','content','image')
        labels={'title':'Заголовок','description':'Краткое содержание','content':'Полное содержание','image':'Картинка'}