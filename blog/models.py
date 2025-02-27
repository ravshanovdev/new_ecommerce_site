from django.db import models
# from django.contrib.auth.models import User
from accounts.models import CustomUser
# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver


class DateTimes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Product(DateTimes):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"mahsulot nomi: {self.name}, narxi: {self.price} so'm"


class Cart(DateTimes):
    user_identifier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_identifier} - {self.total_price}"


class CartItems(DateTimes):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"user: {self.user}, product: {self.product_id.name}, quantity: {self.quantity}, price: {self.price}"


CHOICE_METHOD = (
    ("pending", "Pending"),
    ("completed", "Completed"),
    ("canceled", "Canceled")
)


class Orders(DateTimes):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    delivery_method = models.CharField(max_length=255)
    location = models.CharField(max_length=355)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    status = models.CharField(max_length=150, choices=CHOICE_METHOD)

    def __str__(self):
        return f"name: {self.full_name}, status: {self.status}, location: {self.location}"


CLICK_METHOD = (
    ("click", "Click"),
    ("click pay", "Click Pay")
)


PAYMENT_STATUS = (
    ("pending", "Pending"),
    ("successful", "Successful"),
    ("failed", "Failed")
)


class Payments(DateTimes):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=150, choices=CLICK_METHOD)
    screenshot_url = models.CharField(max_length=150)
    status = models.CharField(max_length=150, choices=PAYMENT_STATUS)

    def __str__(self):
        return f"{self.order_id} - {self.payment_method}"


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product_id.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = CartItems.objects.filter(user=cart_items.user)
    cart_items.total_items = len(total_cart_items)

    cart = Cart.objects.get(id=cart_items.cart_id.id)
    cart.total_price = cart_items.price
    cart.save()


