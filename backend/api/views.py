from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import Product
from django.http import JsonResponse
from products.serializers import ProductSerializer
# Create your views here.

# @api_view(['GET'])
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        # instance = serializer.save()
        # print(instance)
        # data = serializer.data
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': 'not good'}, status=400)
    # model_data = Product.objects.all().order_by('?').first()
    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # data = model_to_dict(model_data)
        # data = model_to_dict(model_data, fields=['id', 'title'])
        # data = ProductSerializer(instance).data
    # return JsonResponse(data)
    # request -> HttpRequest -> Django
    # request.body
    # body = request.body 
    # data = {}
    # try:
    #     data = json.loads(body) # string of json data -> python dict
    # except:
    #     pass    
    # print(data.keys())
    # print(data)
    # data['headers'] = request.headers
    # return JsonResponse({
    #     "message": "Hi there, this is cyndie."
    # })