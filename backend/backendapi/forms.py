from django import forms 
from .models import Order, Stock
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
  
class OrderForm(forms.ModelForm): 
    class Meta: 
        model = Order 
        fields = ['vendor', 'name','number','address','size','note'] 


# class AddStockForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ('vendor','size', 'brand','price' )