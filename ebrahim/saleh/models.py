from django.db import models
from datetime import datetime

from django.db.models import fields


class ebrahim(models.Model):
        
       google_text = models.CharField(max_length=200)
       pub_date = models.DateTimeField('date published')
       description = models.TextField(blank=True)
       your_stoory = models.TextField(blank=True)
       salehw = models.TextField(blank=True)
       salehww = models.TextField(blank=True)
       salehwww = models.TextField(blank=True)
   
    

class saleh(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='goodebrahim', blank=True)
   

    def __str__(self):
        return self.title


class hacker(models.Model):
    treetitle = models.CharField(max_length=50)
    description = models.TextField(blank=True)
     

    def __str__(self):
        return self.treetitle

class product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
   
    def __str__(self):
        return self.title



class news(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
   
    def __str__(self):
        return self.title





class myname(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # your_stoory = models.TextField(blank=True)
    # image = models.ImageField(upload_to='goodebrahim', blank=True)
    def __str__(self):
        return self.title


class bookproduct(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False) # null=True, default=True

    def __str__(self):
        return "%s -  %s" % (self.title, self.description)




# class QuoteCategory(models.Model):
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title

# class Quote(models.Model):
#     quote = models.TextField()
#     author = models.CharField(max_length=200)
    
#     quote_category = models.ForeignKey(
#         'QuoteCategory',
#         on_delete = models.CASCADE
#     )




class book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # description = models.TextField(blank=True)
    # your_stoory = models.TextField(blank=True)
    # salehw = models.TextField(blank=True)

    def __str__(self):
        return self.title










class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=30)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'







class newproduct(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False) # null=True, default=True

    def __str__(self):
        return "%s -  %s" % (self.title, self.description)



class love(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # description = models.TextField(blank=True)
    # your_stoory = models.TextField(blank=True)
    # salehw = models.TextField(blank=True)

    def __str__(self):
        return self.title