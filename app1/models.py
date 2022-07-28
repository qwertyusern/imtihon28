from django.contrib.auth.models import User
from django.db import models

class Suv(models.Model):
    brend=models.CharField(max_length=100)
    narx=models.IntegerField()
    litr=models.IntegerField()
    batafsil=models.TextField(blank=True)

class Mijoz(models.Model):
    ism=models.CharField(max_length=120)
    tel=models.CharField(max_length=70)
    manzil=models.CharField(max_length=220)
    qarz=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Admin(models.Model):
    ism = models.CharField(max_length=120)
    yosh=models.SmallIntegerField()
    ish_vaqti=models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Haydovchi(models.Model):
    ism=models.CharField(max_length=120)
    tel=models.CharField(max_length=70)
    kiritilgan_sana=models.DateField()

class Buyurtma(models.Model):
    suv=models.ForeignKey(Suv,on_delete=models.CASCADE)
    qachon=models.DateTimeField()
    mijoz=models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    miqdor=models.IntegerField()
    umumiy_narx=models.IntegerField()
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)