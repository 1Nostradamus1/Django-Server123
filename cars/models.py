from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    probeg = models.CharField(max_length=300)
    power = models.CharField(max_length=300)
    obiem = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    img = models.CharField(max_length=1000)
    opisanie = models.CharField(max_length=5000)
    hozyain = models.CharField(max_length=300)
    callNumber = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class News(models.Model):
    name = models.CharField(max_length=300)
    anons = models.CharField(max_length=1000)
    full = models.CharField(max_length=10000)
    img = models.CharField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name