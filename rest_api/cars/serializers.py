from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        # fields = ('id','car_name','car_version','car_model')
        fields = '__all__'
        