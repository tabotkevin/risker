from django.db import models
from .enums import types
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Risk(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
 
    class Meta:
        ordering = ('created',)


class Field(models.Model):
    name = models.CharField(max_length=256) # the field name define by user
    risk = models.ForeignKey(Risk, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to={'model__in': ('text', 'number', 'date', 'enum')})
    object_id = models.PositiveIntegerField()
    value = GenericForeignKey('type', 'object_id')
 
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Text(models.Model):
    value = models.TextField()

class Number(models.Model):
    value = models.IntegerField()

class Date(models.Model):
    value = models.DateTimeField()

class Enum(models.Model):
    value = models.CharField(max_length=256, choices=types)
 
    
