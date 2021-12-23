from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Sum



# post
class public_review(models.Model):
    username = models.CharField (max_length=99)
    public_review_unique = models.IntegerField (null=True)
    name = models.CharField (max_length=99)
    p_review = models.TextField (null=True)
    rate = models.CharField (max_length=99,null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class public_contact(models.Model):
    name = models.CharField (max_length=99)
    email = models.CharField (max_length=99)
    p_contact = models.TextField (null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

COLOR_CHOICES = (
       ('garden','garden'),
       ('tree', 'tree'),
       ('vegetable','vegetable'),
       ('flower','flower'),
       ('fruit','fruit'),
    )

class garden_collection(models.Model):
    name = models.CharField (max_length=99)
    category = models.CharField(max_length=99, choices=COLOR_CHOICES, default='green')
    price = models.IntegerField (null = True)
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name



COLOR_CHOICES = (
       ('balcony','balcony'),
       ('rooftop', 'rooftop'),
       ('corporate','corporate'),
    )

class make_your_garden_yourself(models.Model):
    name = models.CharField (max_length=99)
    category = models.CharField (max_length=99,null=True, choices=COLOR_CHOICES, default='corporate')
    price = models.IntegerField ()
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

    @property
    def sum_commitment(self):
        return self.__class__.objects.all().aggregate(sum_all=Sum('price')).get('sum_all')

class your_garden(models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    category = models.CharField (max_length=99,null=True)
    price = models.CharField (max_length=99)
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class fruit_collection(models.Model):
    name = models.CharField (max_length=99)
    price = models.CharField (max_length=99)
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class vegetable_collection(models.Model):
    name = models.CharField (max_length=99)
    price = models.CharField (max_length=99)
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class flower_collection(models.Model):
    name = models.CharField (max_length=99)
    price = models.CharField (max_length=99)
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class tree_collection(models.Model):
    name = models.CharField (max_length=99)
    price = models.CharField (max_length=99)
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name



class all_cart (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    price = models.IntegerField ()
    serial = models.CharField (max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

    @property
    def sum_commitment(self):
        return self.__class__.objects.all().aggregate(sum_all=Sum('price')).get('sum_all')

    

class all_blog (models.Model):
    name = models.CharField (max_length=99)
    title = models.CharField (max_length=99)
    blog = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    photo1 = models.ImageField(null=True, blank=True)
    photo2 = models.ImageField(null=True, blank=True)
    photo3 = models.ImageField(null=True, blank=True)
    photo4 = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        if len(self.blog)>50:
            return self.blog[:50]+"..."
        return self.blog

class portfolio (models.Model):
    title = models.CharField (max_length=99)
    project_details = models.CharField (max_length=99)
    photo = models.ImageField(null=True)
    

    def __str__(self):
        if len(self.project_details)>50:
            return self.project_details[:50]+"..."
        return self.project_details

class order (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    order_id = models.CharField (max_length=99)
    order_serial = models.CharField (max_length=99)
    number = models.CharField (max_length=99)
    transaction_id = models.CharField (max_length=99)

    

    def __str__(self):
        if len(self.order_id)>50:
            return self.order_id[:50]+"..."
        return self.order_id

class about (models.Model):
    name = models.CharField(max_length=99)
    education = models.CharField(max_length=99)
    university = models.CharField(max_length=99)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name
    

