from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_crate = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    #Добавление внешних ключей
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null = True)

    def get_absolute_url(self):
        return f'/post/{self.id}/'
        #return reverse('post',kwargs={'post_id':self.id})

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.id}/'
        #return reverse('category',kwargs={'id':self.id})

class Person(models.Model):
    name = models.CharField(max_length=150,db_index=True,verbose_name='Персона' )
    bron = models.DateField(verbose_name='Дата рождения')
    locic = models.BooleanField(verbose_name='Автор')
    age = models.IntegerField(verbose_name='Возраст')
    test = models.IntegerField(default=None, verbose_name='test')

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Комапании'
        ordering = ['id']

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,db_index=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Продукты'
        verbose_name_plural = 'Продукты'

class Curse(models.Model):
    name=models.CharField(max_length=50, verbose_name='Название курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Курсы'
        verbose_name_plural = 'Курсы'

class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя студента')
    curses =models.ManyToManyField(Curse)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Студенты'
        verbose_name_plural = 'Студенты'
        ordering= ['id']




