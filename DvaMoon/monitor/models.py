from django.db import models

# Create your models here.


class Host_info(models.Model):
    host_id=models.AutoField(primary_key=True)
    ip=models.GenericIPAddressField()
    port=models.IntegerField()
    hostname=models.CharField(max_length=80)

class Redis_name(models.Model):
    name=models.CharField(max_length=64)
    grade=models.IntegerField(null=False)
    item=models.CharField(max_length=32)
