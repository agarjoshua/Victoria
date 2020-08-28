from rest_framework import serializers

from .models import Order
from .models import Complaints
from .models import Stock

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    def perform_create(self, serializer):
        vendor = vendor.objects.get(user=self.request.user)
        return serializer.save(vendor=vendor)

    class Meta:
        model = Order
        fields = ('id','name', 'number','address','size','note')

class StockSerializer(serializers.HyperlinkedModelSerializer):
    vendor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Stock
        fields = ('id','vendor', 'gastype', 'image','price')

class ComplaintsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complaints
        fields = ('id','title', 'body')