from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# @python_2_unicode_compatible
# class Contract(models.Model):


@python_2_unicode_compatible
class Custommer:
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.lastname

@python_2_unicode_compatible
class Period(models.Model):
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "from:{} to:{}".format(self.from_date, self.to_date)


@python_2_unicode_compatible
class Price_Plan(models.Model):
    code = models.IntegerField()

    def __str__(self):
        return self.code

@python_2_unicode_compatible
class Product(models.Model):
    code = models.IntegerField()
    price = models.FloatField()
