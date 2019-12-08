from django.urls import path, include

from shop.views import signup, ProductDetailView, IndexView, order_product, CustomerOrderListView, \
    CustomerOrderDetailView

urlpatterns = [
    path('customers/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('signup/', signup, name="signup"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_id>/order/', order_product, name='order-product'),
    path('orders/', CustomerOrderListView.as_view(), name='customer-order-list'),
    path('orders/<int:pk>/', CustomerOrderDetailView.as_view(), name='customer-order-detail'),
]
