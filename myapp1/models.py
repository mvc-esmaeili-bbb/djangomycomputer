from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=69)
    txt = models.TextField()

    def __str__(self):
        return self.title


class Product1(models.Model):
    title1 = models.CharField(max_length=69)
    txt1 = models.TextField()

    def __str__(self):
        return self.title1
