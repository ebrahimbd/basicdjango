
from django.contrib import admin
from django.urls import path
from saleh import views  
from django.conf.urls import url
from saleh.views import MemberList


# urlpatterns = [
#     path('admin/', admin.site.urls),

# #    path('', home.as_view(), name='home' ),

# path('home/', views.home ),

# ]
urlpatterns = [
    url('home', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('member_list/', MemberList.as_view()),
     url(r'^$', views.eb , name='eb'),
     url('saleh', views.saleh , name='saleh'),
     url('productxx', views.productxx , name='productxx'),
     url('name', views.name , name='name'),
     url('engnews', views.engnews , name='engnews'),
     url('about_view', views.about_view , name='about_view'),
     url('bookproductsview', views.bookproductsview , name='bookproductsview'),
     url('sem', views.sem , name='sem'),
     url('HomeView', views.HomeView , name='HomeView'),
    #  url('member_list', views.member_list , name='member_list'),
     
    
]