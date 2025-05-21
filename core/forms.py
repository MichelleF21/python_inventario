from django import forms
from .models import Product

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'quantity', 'price']

    # def clean_cantidad(self):
    #     quantify = self.cleaned_data['quantity']
    #     if quantify < 1:
    #         raise forms.ValidationError("La cantidad tiene que ser válida.")
    #     return quantify

    def clean_precio(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return price