

from django.db import models
# from django_seed import Seed
# from django.core.validators import MaxValueValidator


class Role(models.Model):
    name = models.CharField(max_length=30)

# Product, Categories, Images, Features, Reviews, Similar

# class Product(models.Model):
#     name = models.CharField(max_length=30)
#     price = models.FloatField()
#     old_price = models.FloatField()
#     description_product = models.TextField(max_length=500, null=True)
#     count = models.IntegerField()
#
#
# class Categories(models.Model):
#     name = models.CharField(max_length=30)
#     description = models.CharField(max_length=500, null=True)
#     product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, default=1)
#
#
# class Images(models.Model):
#     name = models.CharField(max_length=100)
#     path = models.CharField(max_length=100)
#     product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, default=1)
#
#
# class Features(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=100, null=True)
#     product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, default=1)
#
#
# class Reviews(models.Model):
#     user_name = models.CharField(max_length=30, default='anonymous')
#     user_comment = models.TextField(max_length=500, default='no')
#     user_rating = models.IntegerField(validators=[MaxValueValidator(9)])
#     date = models.DateTimeField()
#     product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, default=1)
#
#
# class Similar(models.Model):
#     product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, related_name='product_original', default=1)
#     sim_product = models.ForeignKey('Products', on_delete=models.DO_NOTHING, related_name='product_similar', default=1)
#
