from django.db import models
from datetime import datetime

# 1. Taking Model fields such as [ name, description, image, file ]
# Create User
# Perform CRUD operations and count the number of objects in the database.
# Take a model field write it to the database and perform an automatic
# delete operation.
# Write Tests.
# Dockerize
# Write settings file for production level and local level.
# Document it

# Create your models here.


def user_directory_path(instance, filename: str):
    new_name = str(filename) + datetime.now().strftime("%Y/%m/%d/%I_%M_%S_%f")
    # file will be uploaded to MEDIA_ROOT / user_<id>/<2022_11_01-19_55_22>
    return 'user_{id}/{name}'.format(id=instance.user.id, name=new_name)


class User(models.Model):
    username = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/' +
                              str(user_directory_path))
    file = models.FileField(upload_to='files/' +
                            str(user_directory_path))

    def __str__(self):
        return self.username
