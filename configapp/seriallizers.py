from rest_framework import serializers
from .models import Category, Supplier, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description', 'picture']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id', 'company_name', 'contact_name', 'contact_title', 'address',
            'city', 'region', 'postal_code', 'country', 'phone', 'fax', 'homepage'
        ]


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), source='supplier',
                                                     write_only=True, required=False, allow_null=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category',
                                                     write_only=True, required=False, allow_null=True)

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'supplier', 'supplier_id',
            'category', 'category_id', 'quantity_per_unit', 'unit_price',
            'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued'
        ]
