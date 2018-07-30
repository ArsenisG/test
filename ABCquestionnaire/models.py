from django.db import models
from django.contrib.auth.models import User
	  
class Value(models.Model):
      # SN=models.CharField(max_length=10, blank=True, verbose_name='StudentNumber')
      choice1=models.CharField(max_length=2, blank=True, verbose_name="V1")
      choice2=models.CharField(max_length=2, blank=True, verbose_name="V2")
      choice3=models.CharField(max_length=2, blank=True, verbose_name="V3")
      choice4=models.CharField(max_length=2, blank=True, verbose_name="V4")
      choice5=models.CharField(max_length=2, blank=True, verbose_name="V5")
      choice6=models.CharField(max_length=2, blank=True, verbose_name="V6")
      choice7=models.CharField(max_length=2, blank=True, verbose_name="V7")
      choice8=models.CharField(max_length=2, blank=True, verbose_name="V8")
      choice9=models.CharField(max_length=2, blank=True, verbose_name="V9")
      choice10=models.CharField(max_length=2, blank=True, verbose_name="V10")
      choice11=models.CharField(max_length=2, blank=True, verbose_name="V11")
      choice12=models.CharField(max_length=2, blank=True, verbose_name="V12")
      choice13=models.CharField(max_length=2, blank=True, verbose_name="V13")
      choice14=models.CharField(max_length=2, blank=True, verbose_name="V14")
      choice15=models.CharField(max_length=2, blank=True, verbose_name="V15")
      choice16=models.CharField(max_length=2, blank=True, verbose_name="V16")
      choice17=models.CharField(max_length=2, blank=True, verbose_name="V17")
      user=models.ForeignKey(User, on_delete=models.CASCADE)
      