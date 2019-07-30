from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect,ensure_csrf_cookie
from django.views.generic import View,UpdateView
from .models import Company,Rangi
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.decorators import method_decorator


# Create your views here.

class home(View):
    model = Company
    template_name = 'rangi/home.html'

    def get(self, request):
        form = self.model(None)
        return render(request, self.template_name, {'form': form})


class CreateRangi(View):
    template_name = "rangi/create_rangi.html"
    def get(self,request):
        company = Company.objects.all()

        return render(request,self.template_name,{'company':company})

    def post(self,request):
        color_type = request.POST['color_type']
        rangi = request.POST['rangi']
        brandId = request.POST['brand']
        brand =  Company.objects.get(id = brandId)
        print(brand)
        Rangi.objects.create(
            color_type = color_type,
            rangi = rangi,
            brand = brand
        )

        return HttpResponse('')

class CreateCompany(View):

    template_name = "rangi/create_company.html"
    def get(self,request):

        return render(request,self.template_name)

    def post(self,request):

        company_name = request.POST['company_name']
        print(company_name)
        location = request.POST['location']
        Company.objects.create(
            company_name = company_name,
            location=location,
        )

        return HttpResponse('')




class CreateUser(View):
    template_name = 'rangi/register.html'

    def get(self,request):
        return render(request,'rangi/register.html')

    @method_decorator(ensure_csrf_cookie, name="dispatch")
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create(
            username = username,
            email = email,
            password = password
        )
        return HttpResponse('')


