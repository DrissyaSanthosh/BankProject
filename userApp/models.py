from django.db import models

# Create your models here.
class UserManage(models.Model):
    username =models.CharField(max_length=32, null=True, blank=True)
    password =models.CharField(max_length=32, null=True, blank=True)
    conformpassword =models.CharField(max_length=100, null=True, blank=True)
  
    class Meta:
        db_table='usermanage'