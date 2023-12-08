from datetime import date, datetime
import http
from unicodedata import category
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import BlogForm, ContactForm, ProductForm 
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog, Phone
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария

# Create your views here.


def index_page(request):
    return render(request, 'links.html')

def videopost(request):
    return render(request, 'videopost.html')

def about_page(request):
     return render(request, 'about.html')

def contacts_page(request):
     return render(request, 'contacts.html')

def phones_page(request):
     return render(request, 'phones.html')

def anketa(request):
    assert isinstance(request, HttpRequest) 
    data=None
    gender={'1':'Мужчина', '2': 'Женщина'}
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data=dict()
            data['name']=form.cleaned_data['name']
            data['city']=form.cleaned_data['city']
            data['job']=form.cleaned_data['job']
            data['gender']=form.cleaned_data['gender']
            data['email']=form.cleaned_data['email']
            if(form.cleaned_data['notice']==True):
                data['notice']='Да'
            else:
                data['notice']='Нет'
            data['message']=form.cleaned_data['message']
            form=None
    else:
        form=ContactForm()
    return render(
        request,
        'contacts.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff=False
            reg_f.is_active=True
            reg_f.is_superuser=False
            reg_f.date_joined=datetime.now()
            reg_f.last_login=datetime.now()
            
            regform.save()

            return redirect('/')
    else:
        regform=UserCreationForm()
        
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'registration.html',
        {
            'regform':regform,
            'year':datetime.now().year
        }
    )
            
def blog(request):
    posts=Blog.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog.html',
        {
            'title':'Блог',
            'posts':posts,
            'year':datetime.now().year
        }
    )

def phones(request):
    posts=Phone.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'phones.html',
        {
            'title':'Смартфоны',
            'posts':posts,
            'year':datetime.now().year
        }
    )

def phonesCam(request):
    posts=Phone.objects.filter(category='Камера')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'phones.html',
        {
            'title':'Смартфоны',
            'posts':posts,
            'year':datetime.now().year
        }
    )

def phonesCPU(request):
    posts=Phone.objects.filter(category='Процессор')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'phones.html',
        {
            'title':'Смартфоны',
            'posts':posts,
            'year':datetime.now().year
        }
    )

def phonesTop(request):
    posts=Phone.objects.filter(category='Корпус')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'phones.html',
        {
            'title':'Смартфоны',
            'posts':posts,
            'year':datetime.now().year
        }
    )


def blogpost(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1=Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария   
    else:
        form = CommentForm() # создание формы для ввода комментария
    return render(
        request,
        'blogpost.html',
        {
            'post_1':post_1,
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year
        }
    )

def phone(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1=Phone.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Phone.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('phone', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария   
    else:
        form = CommentForm() # создание формы для ввода комментария
    return render(
        request,
        'phone.html',
        {
            'post_1':post_1,
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year
        }
    )
            
def newpost(request):
    assert isinstance(request,HttpRequest)
    if request.method=="POST":
        blogform=BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f=blogform.save(commit=False)
            blog_f.posted=datetime.now()
            blog_f.autor = request.user
            blog_f.save()
            
            return redirect('blog')
        
    else:
        blogform=BlogForm()
    
    return render(
        request,
        'newpost.html',
        {
            'blogform':blogform,
            'title':'Добавить статью блога',
            'year':datetime.now().year
        }
    )

def newproduct(request):
    assert isinstance(request,HttpRequest)
    if request.method=="POST":
        blogform=ProductForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f=blogform.save(commit=False)
            blog_f.posted=datetime.now()
            blog_f.autor = request.user
            blog_f.save()
            
            return redirect('blog')
        
    else:
        blogform=ProductForm()
    
    return render(
        request,
        'newproduct.html',
        {
            'productform':blogform,
            'title':'Добавить статью блога',
            'year':datetime.now().year
        }
    )