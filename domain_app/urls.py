from django.urls import path
from .views import index, ProductCountAPIView,  AllProductAPIView

urlpatterns = [
    path('', index, name='index'),
    path('product', ProductCountAPIView.as_view()),
    path('all', AllProductAPIView.as_view())
]
