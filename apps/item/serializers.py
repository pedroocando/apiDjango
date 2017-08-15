from rest_framework import serializers
from .models import Item

# serializer for class Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_name', 'item_description', 'item_cost')
