from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Cars, News


class CarsModel:
    def __init__(self, name, price, probeg, power, obiem, year, color, img, opisanie, hozyain, callNumber):
       self.name = name
       self.price = price
       self.probeg = probeg
       self.power = power
       self.obiem = obiem
       self.year = year
       self.color = color
       self.img = img
       self.opisanie = opisanie
       self.hozyain = hozyain
       self.callNumber = callNumber

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"


class NewsModel:
    def __init__(self, name, anons, full, img):
       self.name = name
       self.anons = anons
       self.full = full
       self.img = img


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
