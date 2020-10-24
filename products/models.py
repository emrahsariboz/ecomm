from django.db import models

from django import forms
# Create your models here.


class usertable(models.Model):
	username = models.CharField(max_length = 100)
	email= models.EmailField(max_length=100, default="")

	def __str__(self):
		return self.username
	class Meta:
		db_table = "user_table"


class ProductTable(models.Model):
	product_name = models.CharField(max_length=200)
	product_descryption = models.CharField(max_length=200)
	manufacturar_name = models.CharField(max_length = 200)
	inventory_count = models.IntegerField()


	def __str__(self):
		return self.product_name
	class Meta:
		db_table = "products_table"




class order(models.Model):
	product_id = models.AutoField(max_length=30, primary_key = True)
	user_id = models.ForeignKey(usertable, null=True, on_delete=models.CASCADE)
	product_name = models.ForeignKey(ProductTable, null=True, on_delete=models.SET_NULL)
	quantity = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add = True, null=True)
	
	def __str__(self):
		return self.product_name.product_name

	class Meta:
		db_table = "products_bought_table"
