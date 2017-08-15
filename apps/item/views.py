from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo")

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        json = {'message':'Item do NOT exist'}
        return Response(json,status=status.HTTP_404_NOT_FOUND)

    # get details of a single Item
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        json = {'message':
                'successful search','item':serializer.data}
        return Response(json,status.HTTP_200_OK)
    # delete a single Item
    elif request.method == 'DELETE':
        item.delete()
        json = {'message':
                'Item deleted successfully'}
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single Item
    elif request.method == 'PUT':
        data = {
            'item_name': request.data.get('name'),
            'item_description': request.data.get('desc'),
            'item_cost': request.data.get('cost')
        }
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            json = {'message':'Item updated successfully',
                    'item':serializer.data}
            return Response(json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_items(request):
    # get all Items
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        json = {'items':serializer.data}
        return Response(json,status.HTTP_200_OK)
    # insert a new record for a Item
    elif request.method == 'POST':
        data = {
            'item_name': request.data.get('name'),
            'item_description': request.data.get('desc'),
            'item_cost': request.data.get('cost')
        }
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json = {'message':'Item created successfully','item':serializer.data}
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
