from django.conf.urls import url

from apps.item.views import *

urlpatterns = [
    url(r'^$', index),
    url(
        r'^items/(?P<pk>[0-9]+)$',
        get_delete_update_item,
        name='get_delete_update_item'
    ),
    url(
        r'^items',
        get_post_items,
        name='get_post_items'
    ),
]
