from django.urls import path, include

from shop.views import index, signup

urlpatterns = [
    path('customers/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('signup/', signup, name="signup")
]
