from django.shortcuts import render, redirect
from .forms import orderForm, CreateUserForm, saveUserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages


# @login_required(login_url = 'login')
# def createOrder(request):

# 	form = orderForm()

# 	if request.method == "POST":
# 		form = orderForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'products/order_form.html', context)

def registerPage(request):

	# if request.user.is_authenticated:
	# 	return redirect('home')

	form = CreateUserForm()
	form2 = saveUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		form2 = saveUserForm(request.POST)
		if form.is_valid():
			form.save()
			form2.save()
			return redirect('login')

	context = { 'form':form }
	return render(request, "products/register.html", context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password1")

		user = authenticate(request, username=username, password= password)

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'username or password is incorrect!')


	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()


	context = { 'form':form }
	return render(request, "products/login.html", context)


@login_required(login_url = 'login')
def home(request):
	orders = order.objects.all()
	customers = usertable.objects.all()

	total_order = orders.count()

	context = {
			'orders':orders,
		    'customers':customers,
		    'total_order':total_order
	}

	return render(request, "products/home.html",context)



@login_required(login_url = 'login')
def productPage(request):
	# ProductTable is the name of db table
	# products variable needs to be passed to list
	products = ProductTable.objects.all()


	return render(request, "products/list.html", {'products': products})

@login_required(login_url = 'login')
def Customer(request, pk):
	customer_info = usertable.objects.get(id=pk)

	orders = customer_info.order_set.all()

	total_orders = orders.count()



	context = {
			'customer_info':customer_info,
		    'orders':orders,
		    'total_orders':total_orders
	}



	return render(request, "products/customer.html", context)


@login_required(login_url = 'login')
def createOrder(request):

	form = orderForm()

	if request.method == "POST":
		form = orderForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'products/order_form.html', context)

@login_required(login_url = 'login')
def updateOrder(request, pk):

	orders = order.objects.get(user_id_id=pk)
	form = orderForm(instance=orders)

	if request.method == "POST":
		form = orderForm(request.POST, instance=orders)

		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'products/order_form.html', context)

@login_required(login_url = 'login')
def deleteOrder(request, pk):
	orders = order.objects.get(product_id=pk)
	if request.method == "POST":
		orders.delete()
		return redirect('/')

	context = {'item': orders}
	return render(request, 'products/delete.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')