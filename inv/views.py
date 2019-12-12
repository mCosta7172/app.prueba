from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

from bases.views import SinPrivilegios, VistaBaseCreate, VistaBaseEdit

class CategoriaView(SinPrivilegios, generic.ListView ):
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'


class CategoriaNew(VistaBaseCreate):
    permission_required = 'inv.add_categoria'
    model = Categoria
    template_name='inv/categoria_form.html'
    form_class=CategoriaForm
    success_url=reverse_lazy('inv:categoria_list')

class CategoriaEdit(VistaBaseEdit):
    permission_required = 'inv.change_categoria'
    model = Categoria
    template_name='inv/categoria_form.html'
    form_class=CategoriaForm
    success_url=reverse_lazy('inv:categoria_list')

class CategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = 'inv.delete_categoria'
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy('inv:categoria_list')


class SubCategoriaView(SinPrivilegios, generic.ListView ):
    permission_required = 'inv.view_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'


class SubCategoriaNew(VistaBaseCreate):
    permission_required = 'inv.add_subcategoria'
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name='obj'
    form_class=SubCategoriaForm
    success_url=reverse_lazy('inv:subcategoria_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(VistaBaseEdit):
    permission_required = 'inv.change_subcategoria'
    model = SubCategoria
    template_name='inv/subcategoria_form.html'
    context_object_name='obj'
    form_class=SubCategoriaForm
    success_url=reverse_lazy('inv:subcategoria_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = 'inv.delete_subcategoria'
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy('inv:subcategoria_list')


class MarcaView(SinPrivilegios, generic.ListView ):
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'

class MarcaNew(SinPrivilegios, generic.CreateView):
    permission_required = 'inv.add_marca'
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name='obj'
    form_class=MarcaForm
    success_url=reverse_lazy('inv:marca_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = 'inv.change_marca'
    model = Marca
    template_name='inv/marca_form.html'
    context_object_name='obj'
    form_class=MarcaForm
    success_url=reverse_lazy('inv:marca_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name='inv/catalogos_del.html'
    if not marca:
        return redirect('inv:marca_list')
    if request.method=='GET':
        contexto={'obj':marca}
    if request.method=='POST':
        marca.estado=False
        marca.save()
        messages.success(request, 'Marca Inactivada.')
        return redirect('inv:marca_list')
    return render(request,template_name, contexto)

class UMView(SinPrivilegios, generic.ListView ):
    permission_required = 'inv.view_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'


class UMNew(SinPrivilegios, generic.CreateView):
    permission_required = 'inv.add_unidadmedida'
    model = UnidadMedida
    template_name='inv/um_form.html'
    context_object_name='obj'
    form_class=UMForm
    success_url=reverse_lazy('inv:um_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UMEdit(SinPrivilegios, generic.UpdateView):
    permission_required = 'inv.change_unidadmedida'
    model = UnidadMedida
    template_name='inv/um_form.html'
    context_object_name='obj'
    form_class=UMForm
    success_url=reverse_lazy('inv:um_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidadmedida', login_url='bases:sin_privilegios')
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name='inv/catalogos_del.html'
    if not um:
        return redirect('inv:um_list')
    if request.method=='GET':
        contexto={'obj':um}
    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect('inv:um_list')
    return render(request,template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView ):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'


class ProductoNew(SinPrivilegios, generic.CreateView):
    permission_required = 'inv.add_producto'
    model = Producto
    template_name='inv/producto_form.html'
    context_object_name='obj'
    form_class=ProductoForm
    success_url=reverse_lazy('inv:producto_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(VistaBaseEdit):
    permission_required = 'inv.change_producto'
    model = Producto
    template_name='inv/producto_form.html'
    form_class=ProductoForm
    success_url=reverse_lazy('inv:producto_list')

    def form_invalid(self, form):
        print("form is invalid")
        return super().form_invalid(form)
        

    



@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name='inv/catalogos_del.html'
    if not prod:
        return redirect('inv:producto_list')
    if request.method=='GET':
        contexto={'obj':prod}
    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect('inv:producto_list')
    return render(request,template_name, contexto)

