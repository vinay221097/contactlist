from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Contacts(models.Model):
	name=models.CharField(max_length=200,blank=False)
	email=models.CharField(max_length=200,blank=False)
	# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=15, blank=True) # validators should be a list

	def __str__(self):
		return self.name