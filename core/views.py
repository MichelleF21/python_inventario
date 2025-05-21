from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from .models import Product
from .forms import ProductoForm


# Para listar productos
def listar_productos(request):
    productos = Product.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

# Para crear un nuevo producto
class CrearProductoView(View):
    form_class = ProductoForm
    template_name = 'crear_producto.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
        return render(request, self.template_name, {'form': form})

# Para eliminar un producto
def eliminar_producto(request, producto_id):
    product = get_object_or_404(Product, pk=producto_id)
    if request.method == 'POST':
        product.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': product})


