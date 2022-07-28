from rest_framework import serializers
from .models import *

class SuvSer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = "__all__"
class MijozSer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"
class AdminSer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class HaydovchiSer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"

class BuyurtmaSer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"