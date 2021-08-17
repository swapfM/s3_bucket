from django.db import models
from django.contrib.auth.models import User
import os


def update_filename(instance, filename):
    path = ""
    format = instance.UserName+".mp4"
    return os.path.join(path, format)



class UserModel(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Pic = models.FileField(null=True, upload_to=update_filename)

    # def delete(self):
    #     self.filefield.delete(save=False)
    # super().delete()


    def __str__(self):
        return self.UserName

