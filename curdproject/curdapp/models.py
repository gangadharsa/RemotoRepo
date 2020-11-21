from django.db import models

# Create your models here.
class StudentData(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=10)
    class_name=models.CharField(max_length=5)
    section=models.CharField(max_length=2)
    mob=models.BigIntegerField()
    email=models.EmailField( max_length=50)
    odia=models.IntegerField()
    hindi=models.IntegerField()
    eng=models.IntegerField()
