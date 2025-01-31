from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title 
        serializer.save(content=content) 

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
   queryset = Product.objects.all() 
   serializer_class = ProductSerializer
   
product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
   queryset = Product.objects.all() 
   serializer_class = ProductSerializer
   
product_update_view = ProductListAPIView.as_view()  

class ProductUpdateAPIView(generics.UpdateAPIView):
   queryset = Product.objects.all() 
   serializer_class = ProductSerializer
   lookup_field = 'pk'
   
   def perform_update(self, serializer):
       instance = serializer.save()
       if not instance.content:
           instance.content = instance.title
           instance.save()
   
product_update_view = ProductUpdateAPIView.as_view()    

class ProductDestroyAPIView(generics.DestroyAPIView):
   queryset = Product.objects.all() 
   serializer_class = ProductSerializer
   lookup_field = 'pk'
   
   def perform_destroy(self, instance):
       super().perform_destroy(instance)
    #    instance = serializer.save()
    #    if not instance.content:
    #        instance.content = instance.title
    #        instance.save()
   
product_destroy_view = ProductDestroyAPIView.as_view()


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.list(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()        

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 
   
    if method == 'GET':
        if pk is not None:
           # detail view
           obj = get_object_or_404(Product, pk=pk)
           data = ProductSerializer(obj, many=False).data
           return Response(data)
        # url_args?
        # get request -> detail view
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
       
    if method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)  # form.save() -> Product.objects.create()
            
            # instance = serializer.save()
            # instance = form.save()
            # print(serializer.data)
            return Response(serializer.data)
        return Response({'invalid': 'not good'}, status=400)