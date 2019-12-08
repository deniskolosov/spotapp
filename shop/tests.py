import factory
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Customer, Order, Product, Producer


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user%s' % n)

    class Meta:
        model = User


class CustomerFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'user%s' % n)
    email = factory.Sequence(lambda n: 'user%s@example.com' % n)

    class Meta:
        model = Customer


class ProducerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Producer


class ProductFactory(factory.DjangoModelFactory):
    producer = factory.SubFactory(ProducerFactory)

    class Meta:
        model = Product


class OrderFactory(factory.DjangoModelFactory):
    customer = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = Order


class CustomerModelTests(TestCase):
    def test_create_user_creates_customer(self):
        user = UserFactory()
        self.assertTrue(Customer.objects.filter(user=user.id).exists())


class CustomerOrderListViewTest(TestCase):
    def test_view(self):
        client = Client()
        user = UserFactory()
        another_user = UserFactory()
        order = OrderFactory(customer=user.customer)
        another_order = OrderFactory(customer=another_user.customer)
        client.force_login(user=user)
        response = client.get(reverse('customer-order-list'))
        self.assertTrue(response.status_code, 200)
        customer_orders = list(response.context[-1]['customer_orders'])

        # Assert that we filter orders by customer
        self.assertTrue(order in customer_orders)
        self.assertTrue(another_order not in customer_orders)
