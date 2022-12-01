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
    name, ext = filename.split('.')
    # to make sure file is always unique
    timestamps = datetime.now().strftime("%Y/%m/%d/%I_%M_%S_%f")
    new_name = str(name) + timestamps + '.' + str(ext)
    # file will be uploaded to MEDIA_ROOT / user_<id>/<2022_11_01-19_55_22>
    return 'user/{username}/{name}'.format(
        username=instance.username,
        name=new_name
    )


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=user_directory_path)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.username
