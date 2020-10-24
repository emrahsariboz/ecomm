from django.forms import ModelForm
from .models import order, usertable
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User

class orderForm(ModelForm):
	class Meta:
		# Name of modedl
		model = order
		# Which fields --> __all__
		fields = '__all__'



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email','password1','password2']



class saveUserForm(ModelForm):
	class Meta:
		# Name of modedl
		model = usertable
		# Which fields --> __all__
		fields =['username', 'email']
