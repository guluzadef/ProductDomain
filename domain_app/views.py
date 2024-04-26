from django.http import HttpResponse
from pymongo import MongoClient
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductDomain
from .helper.database import MyMongo



def index(request):
    # delete = MyMongo.delete_all('productdomain')
    for product in ProductDomain.objects.all():
        product_data = {
            'name': product.name,
            'price': float(product.price),
            'category': str(product.category),
            'parent': product.category.parent.name if product.category.parent else None
        }
        MyMongo.save('productdomain', product_data)
    return HttpResponse('mytest1234')

class AllProductAPIView(APIView):
    def get(self, request):
        all_data = MyMongo.find_all('productdomain')
        response_data = []
        for data in all_data:
            data.pop('_id', None)
            response_data.append(data)
        return Response(response_data)

class ProductCountAPIView(APIView):
    def get(self, request):
        min_price = float(request.query_params.get('min_price', 0))
        max_price = float(request.query_params.get('max_price', float('inf')))
        all_data = MyMongo.search('productdomain', min_price, max_price)
        category_counts = {}
        for item in all_data:
            if item['parent'] is not None:
                category_name = item['category']
                category_counts[category_name] = category_counts.get(category_name, 0) + 1
        return Response(category_counts)
