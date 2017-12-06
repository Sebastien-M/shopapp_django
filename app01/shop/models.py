from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Custommer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.CharField(max_length=20)
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.lastname


@python_2_unicode_compatible
class Period(models.Model):
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='period', default='')

    def __str__(self):
        return self.from_date


@python_2_unicode_compatible
class Product(models.Model):
    code = models.CharField(default='', max_length=100)
    price = models.FloatField()
    description = models.TextField(default='')

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class PricePlan(models.Model):
    code = models.CharField(default='', max_length=100)
    products = models.ManyToManyField(Product, related_name='products')
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='price_plan')

    def __str__(self):
        return self.code


    @property
    def get_price(self):
        total = 0
        for product in self.products.all():
            total += product.price

        return total
    
@python_2_unicode_compatible
class Contract(models.Model):
    price_plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, default='', related_name='price_plan', db_index=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, default='', related_name='period')
    owner = models.ForeignKey(Custommer, on_delete=models.CASCADE, default='', related_name='owner')

    def __str__(self):
        return self

@python_2_unicode_compatible
class Order(models.Model):
    custommer_first_name = models.CharField(max_length=50);
    custommer_last_name = models.CharField(max_length=50);
    priceplan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, default='', related_name='pp')

    def __str__(self):
        return self.custommer_first_name
