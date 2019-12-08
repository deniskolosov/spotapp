from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic

from shop.forms import CustomerForm
from shop.models import Product, Order


class IndexView(LoginRequiredMixin, generic.ListView):
    """Home page view with list of available Products."""
    template_name = 'index.html'
    context_object_name = 'products'
    model = Product


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    """ Product detail view with description"""
    model = Product
    template_name = 'product_detail.html'


class CustomerOrderListView(LoginRequiredMixin, generic.ListView):
    """List of Orders made by Customer."""
    model = Order
    context_object_name = 'customer_orders'
    template_name = 'customer_orders_list.html'

    def get_queryset(self):
        return Order.objects.select_related(
            'customer', 'product').filter(customer=self.request.user.customer)


class CustomerOrderDetailView(LoginRequiredMixin, generic.DetailView):
    """Detail page view for order made by Customer."""
    model = Order
    context_object_name = 'customer_order'
    template_name = 'customer_order_detail.html'


def signup(request):
    """Creates user using CustomerForm."""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.name = form.cleaned_data.get('name')
            user.customer.email = form.cleaned_data.get('email')
            user.save()
            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomerForm()
    return render(request, 'signup.html', {'form': form})


def order_product(request, product_id):
    """Orders product and displays message."""
    product = get_object_or_404(Product, pk=product_id)
    customer = request.user.customer
    Order.objects.create(customer=customer, product=product)
    messages.success(request, 'Продукт был добавлен в заказ!')
    return HttpResponseRedirect(reverse('index'))
