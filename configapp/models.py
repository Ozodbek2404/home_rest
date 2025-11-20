from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='category_pics/', blank=True, null=True)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    company_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200, blank=True, null=True)
    contact_title = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    units_in_stock = models.IntegerField(default=0)
    units_on_order = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
