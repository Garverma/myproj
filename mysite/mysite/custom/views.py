from django.http.response import HttpResponse
from django.shortcuts import render
from ecom.models import Product,Category
from django.views import generic
from django.contrib.auth.models import User
from .forms import CReg
'''def home(request):
    c=Category.objects.all()
    return render(request,"custom/home.html",{'cat':c})
'''

class Home(generic.ListView):
    template_name="custom/home.html"
    context_object_name='cat'
    def get_queryset(self):
        return Category.objects.all()
    
class Register(generic.Views):
    def get(self,request):
        return render(request,"custom/reg.html",{'form':CReg(None)})
    def post(self,request):
        f=CReg(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get("password")
            data.set_password(p)
            data.save()
            return HttpResponse("user created")
        return render(request,"custom/reg.html",{'form':f})