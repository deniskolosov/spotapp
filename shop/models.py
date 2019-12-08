from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Producer(models.Model):
    """Producer produce Products."""
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"{}"'.format(self.name)


class Customer(models.Model):
    """Customer makes Orders."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Customer #{}".format(self.id)


class Product(models.Model):
    """Product is a part of an Order and produced by Producer."""
    name = models.CharField(max_length=256)
    description = models.TextField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return "/products/%i/" % self.id


class Order(models.Model):
    """Order contains products"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def update_customer_signal(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()
