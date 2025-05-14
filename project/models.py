from django.db import models

class userdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='')


class contactdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    address = models.TextField()
    image = models.ImageField(upload_to='images/', default='')
    user_id = models.ForeignKey(userdata, on_delete=models.CASCADE, default=1)



