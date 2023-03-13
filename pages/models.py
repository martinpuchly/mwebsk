from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titulok", max_length=255,  null=False, blank=False)
    slug = models.SlugField(verbose_name="URL link", unique=True)
    body = RichTextField(verbose_name="Stránka", null=False, blank=False)
    views = models.IntegerField(default=0, null=True)
    publised = models.BooleanField(verbose_name="publikované?", default=True)
    description = models.CharField(verbose_name="popis", max_length=255,  null=True, blank=True)
    keywords = models.CharField(verbose_name="kľúčové slová", max_length=255,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "stránka"
        verbose_name_plural = "stránky"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(Page, self).save(*args, **kwargs)



class Tag(models.Model):
    title = models.CharField(verbose_name="Titulok", max_length=255,  null=False, blank=False)
    slug = models.SlugField(verbose_name="URL link", unique=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tagy"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(verbose_name="Titulok", max_length=255,  null=False, blank=False)
    slug = models.SlugField(verbose_name="URL link", unique=True)
    intro = RichTextField(verbose_name="Úvod článku/Krátky článok", null=False, blank=False)
    body = RichTextField(verbose_name="Článok", null=True, blank=True)  
    tags = models.ManyToManyField(Tag, verbose_name="tagy", blank=True)
    views = models.IntegerField(default=0, null=True)
    likes = models.IntegerField(default=0, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publised = models.BooleanField(verbose_name="publikovať", default=True)
    publised_at = models.DateTimeField(verbose_name="publikovať", null=True, blank=True)
    description = models.CharField(verbose_name="popis", max_length=255,  null=True, blank=True)
    keywords = models.CharField(verbose_name="kľúčové slová", max_length=255,  null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "článok"
        verbose_name_plural = "články"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class QuickNew(models.Model):
    title = models.CharField(verbose_name="Titulok", max_length=25, null=True, blank=True)
    text = models.CharField(verbose_name="Text rýchlej novinky", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        title = f"{self.title} - " if self.title != None else ""
        return f"{title} {self.text}"

    class Meta:
        verbose_name = "rýchla novinka"
        verbose_name_plural = "rýchle novinky"