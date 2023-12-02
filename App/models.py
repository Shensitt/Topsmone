from functools import _Descriptor
from msilib.schema import Verb
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(msx_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")
    
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
