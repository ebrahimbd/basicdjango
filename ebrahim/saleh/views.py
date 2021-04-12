 
from typing import ContextManager
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponse, request
from .models import hacker , product , myname , news, bookproduct, book , Member
from .forms import ProductForm



def home(request):

 return HttpResponse("ddddddddddddddddddddddddddddddddd")

def eb (request):
    return render( request,'eb.html')

for i in range(5):
      print("fuck u google i need job google")




# def bookproductsview(request):
#      form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save() 
#     context = {
#         'form': form
#     }
#     return render( request,'bookproduct.html', context)


def bookproductsview(request):
     
    obj = bookproduct.objects.get(id=3)
    vtext = {
        'ami':obj 
    }
    return render( request,'bookproduct.html', vtext)





def saleh(request):
    obj = hacker.objects.get(id=1)
    context = {
        'object':obj.treetitle,
    }
    return render( request,'eb.html', context)




# def productxx(request):
#     obj = product.objects.get(id=3)
#     context = {
#         'product':obj 
#     }
#     return render( request,'product.html', context)


def productxx(request):
    
    mode = product.objects.all()
    context = {
        'productqq': mode
    }
    return render( request,'product.html', context)


     
     


def name(request):
    nam = myname.objects.get(id=4)
 
    amartext = {
        'amarnam':  nam 
    }
    return render( request,'eb.html', amartext)


def about_view(request):
    my_context = {
        "ebrahim": "my name is ebrahim",
        "this_is_true": True,
        "my_phone": 17953747512 ,
        "my_list": [1313, 4231, 312, "Abc"],
        'myname': "ebrahim",
        "my_html": "<h1> Hello World </h1>"

    }
    return render(request, "about.html", my_context)


def engnews(request):
    objt = news.objects.get(id=1)
    contexz = {
        'newsx':objt 
    }
    return render( request,'news.html', contexz )


# class engnews(ListView):
#     template_name = "news.html"
#     model = news

#     def get_queryset(self):
#         query_set = super().get_queryset()
#         return query_set.select_related('title')



# def add(request):
#        va1 =int(request.GET["num1"])
#        va2 = int(request.GET["num1"])
#        res = (va1 + va2)

#        return render(request, 'result.html', {'ebrahim':res})


def sem(request):
       va1 =int( request.POST["num1"])
       va2 = int(request.POST["num2"])
       res = int( va1 + va2)

       return render(request, 'result.html', {'ebrahim':res})





# def HomeView(request):
#     objectzx = book.objects.all()
#     asd = {
#         'quote': objectzx
#     }
#     return render(request,'book.html', asd)

def HomeView(request):
    mode = book .objects.all()
    objt  = book.objects.get(id=2)
     
    context = {
        'productqq': mode ,
          'process': objt 
          
    }
  
    return render( request,'book.html', context)






class MemberList(ListView):
    model = Member
    # template_name_suffix = '_get'
    template_name ='ami/student.html'
     
  