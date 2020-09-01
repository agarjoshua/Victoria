from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import OrderSerializer,StockSerializer,ComplaintsSerializer
from .models import Order,Stock,Complaints

#other functionmality related imports for log in forms et al
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm,SignUpForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import AbstractUser

#for log in shenanigans
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from backendapi.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#views to handle the crud requests
from .models import Stock
from django.views.generic import View
from django.http import JsonResponse

#VIEWS FOR FRONT END HOMEPAGE
@login_required
def home(request): 
    orders = Order.objects.all() 
    return render(request, 'backendapi/index.html') 
  

def signup(request):
        register_form = SignUpForm()
        if request.method=='POST':
            register_form = SignUpForm(request.POST)
            if register_form.is_valid():
                # form = SignUpForm(request.POST)
                vendor = Vendor.objects.create_user(
                    username=request.POST['username'], 
                    email=request.POST['email'], 
                    password=request.POST['password1'])

                user.is_active = False
                user.save()

                return HttpResponseRedirect(reverse('index'))

        return render ('registration/registration_form.html', {'form':register_form})


def manage_stock(request):

    stocks = Stock.objects.all
    return render(request,'stock.html',{"stocks":stocks})
    
class CreateStock(View):
    def  get(self, request):
        size = request.GET.get('size', None)
        brand = request.GET.get('brand', None)
        price = request.GET.get('price', None)

        obj = Stock.objects.create(
            size = size,
            brand = brand,
            price = price
        )

        stocks = {'id':obj.id,'size':obj.size,'brand':obj.brand,'price':obj.price}

        data = {
            'stocks': stocks
        }
        # return JsonResponse(data)
        stocks = Stock.objects.all
        return render(request,'stock.html',{"stocks":stocks})


class UpdateStock(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        size = request.GET.get('size', None)
        brand = request.GET.get('brand', None)
        price = request.GET.get('price', None)

        obj = Stock.objects.get(id=id1)
        size = size,
        brand = brand,
        price = price,
        obj.save()

        stocks = {'id':obj.id,'size':obj.size,'brand':obj.brand,'price':obj.price}

        data = {
            'stocks': stocks
        }

        stocks = Stock.objects.all(id=id1)
        return render(request,'stock.html',{"stocks":stocks})

class DeleteStock(View):
    def  get(self, request, pk ,format=None):

        stock = Stock.objects.filter(pk=pk) 

        request.method == 'POST'
        stock.delete()

        stocks = Stock.objects.all()
        return render(request,'stock.html',{"stocks":stocks})



def manage_orders(request):
    orders = Order.objects.all
    return render(request,'orders.html',{"orders": orders})

















#SERIALIZERS
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('name')
    serializer_class = OrderSerializer
    
    def pre_save(self, obj):
        vendor = vendor.objects.get(user=self.request.user)
        return serializer.save(vendor=vendor)
        Order = self.request.user

    # def perform_create(self, serializer):
    #     vendor = vendor.objects.get(user=self.request.user)
    #     return serializer.save(vendor=vendor)

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('gastype')
    serializer_class = StockSerializer

class ComplaintsViewSet(viewsets.ModelViewSet):
    queryset = Complaints.objects.all().order_by('title')
    serializer_class = ComplaintsSerializer