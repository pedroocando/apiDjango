from django.test import TestCase
from ..models import Item


class ItemTest(TestCase):
    """ Test module for Item model """

    def setUp(self):
        Item.objects.create(
            item_name='item1', item_description="descripcion1", item_cost=23.4)
        Item.objects.create(
            item_name='item2', item_description="descripcion2", item_cost=23.4)
