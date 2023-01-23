from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Cart

def home(request):
    return render(request,"app/home.html")

def cart(request):
    context=[]
    return render(request,"app/cart.html")

class CategoryView(View):
    def get(self,request,val):
        product =Product.objects.filter(category=val)
        title =Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product =Product.objects.filter(title=val)
        title =Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())
       
class ProductDetail(View):
    def get(self,request,pk):
     product =Product.objects.get(pk=pk)
     return render(request, "app/productdetail.html",locals())  

     
        
           




    