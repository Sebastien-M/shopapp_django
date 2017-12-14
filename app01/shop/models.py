from django.db import models
from django.utils.encoding import python_2_unicode_compatible

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

    def __str__(self):
        return self.code

    @property
    def get_price(self):
        total = 0
        for product in self.products.all():
            total += product.price

        return total


# @python_2_unicode_compatible
# class Contract(models.Model):
#     price_plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, default='', related_name='price_plan', db_index=True)
#     period = models.ForeignKey(Period, on_delete=models.CASCADE, default='', related_name='period')
#     owner = models.ForeignKey(Custommer, on_delete=models.CASCADE, default='', related_name='owner')
#
#     def __str__(self):
#         return self


@python_2_unicode_compatible
class Order(models.Model):
    custommer_first_name = models.CharField(max_length=50)
    custommer_last_name = models.CharField(max_length=50)
    priceplan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, default='', related_name='pp')

    def __str__(self):
        return self.custommer_last_name
