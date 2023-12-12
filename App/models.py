from tabnanny import verbose
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg',verbose_name='Путь к картинке')

    def get_absolute_url(self):
        return reverse("blogpost",args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "Posts"
        ordering=["-posted"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"
        
admin.site.register(Blog)
# Create your models here.

class Comment(models.Model):
    text = models.TextField(verbose_name = "Текст комментария")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата комментария")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор комментария")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")
    # Методы класса:
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарии к статье блога"
        verbose_name_plural = "Комментарии к статьям блога"
admin.site.register(Comment)

class Phone(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg',verbose_name='Путь к картинке')
    category = models.CharField(max_length=100, verbose_name="Категория")
    summa = models.DecimalField(verbose_name='Стоимость', max_digits=8, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse("phone",args=[str(self.id)])

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "Phones"
        ordering=["-posted"]
        verbose_name = "Смартфон"
        verbose_name_plural = "Смартфоны"
        
admin.site.register(Phone)


class ShoppingCart(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg',verbose_name='Путь к картинке')
    category = models.CharField(max_length=100, verbose_name="Категория")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    summa = models.DecimalField(verbose_name='Стоимость', max_digits=8, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse("shoppingcart",args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "ShoppingCart"
        ordering=["-posted"]
        verbose_name = "Корзина"
        verbose_name_plural = "Товары Корзины"
        
admin.site.register(ShoppingCart)

class Orders(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg',verbose_name='Путь к картинке')
    summa = models.DecimalField(verbose_name='Стоимость', max_digits=8, decimal_places=2, default=0)
    status = models.TextField(verbose_name='Статус', default='В обработке')

    def get_absolute_url(self):
        return reverse("orders",args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "Order"
        ordering=["-posted"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        
admin.site.register(Orders)