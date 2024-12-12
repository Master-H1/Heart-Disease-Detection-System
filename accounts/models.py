from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRole(models.Model):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class UserRoleManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_profile', blank=True, null=True)
    phone = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} --- Role: {self.role}'
