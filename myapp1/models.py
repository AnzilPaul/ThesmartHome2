from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserRegInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number=models.CharField(max_length=15,unique=True,blank=False,null=False)
    home_address=models.TextField(blank=True)
    def __str__(self) -> str:
        return self.user.username

class Operatelog(models.Model):
    status=models.CharField(max_length=3)
    def __str__(self):
        return self.status 