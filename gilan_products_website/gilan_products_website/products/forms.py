from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("phone_number",)


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'description', 'image', 'category']


