from rest_framework import serializers
from .models import MenuItem, Category
from .models import Category
from decimal import Decimal

# class CategorySerializer(serializers.ModelSerializer):
#     # stock = serializers.IntegerField(source='inventory') #use to edit the fields to add new name
#     price_after_task = serializers.SerializerMethodField(method_name='calculate_tax')
#     class Meta:
#         model = MenuItem
#         fields = ['id', 'title', 'price', 'inventory', 'price_after_task', 'category']
        
class MenuItemSerializer(serializers.ModelSerializer):
    # stock = serializers.IntegerField(source='inventory') #use to edit the fields to add new name
    price_after_task = serializers.SerializerMethodField(method_name='calculate_tax')
    category = serializers.StringRelatedField()
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'price_after_task', 'category']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)    
        