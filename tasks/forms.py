from django import forms
from .models import IceCream

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['flavor', 'description', 'price']
        labels = {
            'flavor': 'Вкус мороженого',
            'description': 'Описание мороженого',
            'price': 'Цена',
        }

class MyForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)