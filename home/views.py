from django.db.models.fields import NullBooleanField
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, request
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import all_blog, all_cart, garden_collection, public_review, fruit_collection, vegetable_collection, flower_collection, tree_collection, all_cart, all_blog, portfolio, make_your_garden_yourself, your_garden, order, about
from .models import public_contact
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum


def home(request):
    return render(request, "1_home.html")


def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password incorrect')

    return render(request, '13_login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, '12_singup.html')


def signout(request):
    logout(request)
    return redirect("/")


class review (DetailView):
    template_name = "review.html"
    model = garden_collection
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(review, self).get_context_data(*args, **kwargs)
        context['public_review_list'] = public_review.objects.all()
        return context


def review_form(request):
    if request.method == 'POST':
        public_review_unique = int(request.POST['public_review_unique'])
        username = request.POST['username']
        name = request.POST['name']
        p_review = request.POST['review']
        rate = request.POST['rate']
        if rate == NullBooleanField:
            messages.erroe(
            request, "You have to rate first.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            review_database = public_review(
                username=username, name=name, p_review=p_review, rate=rate, public_review_unique=public_review_unique)
            review_database.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def contact(request):
    return render(request, "contact.html")


def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        p_contact = request.POST['p_message']
        contact_database = public_contact(
            name=name, email=email, p_contact=p_contact)
        contact_database.save()
        messages.success(
            request, "We just received your message will contact you later.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class garden (ListView):
    template_name = "6_garden.html"
    model = garden_collection
    ordering = ['-id']


class fruit (ListView):
    template_name = "7_fruit.html"
    model = garden_collection
    ordering = ['-id']


class vegetable (ListView):
    template_name = "8_vegitable.html"
    model = garden_collection
    ordering = ['-id']


class flower (ListView):
    template_name = "9_flower.html"
    model = garden_collection
    ordering = ['-id']


class tree (ListView):
    template_name = "10_tree.html"
    model = garden_collection
    ordering = ['-id']


class cart (ListView):
    template_name = "cart.html"
    model = all_cart
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super(cart, self).get_context_data(**kwargs)
        context['total_price'] = all_cart.objects.filter(username = self.request.user.username).aggregate(sum_all=Sum('price')).get('sum_all')
        return context

class remove_cart (DeleteView):
    template_name = "remove_cart.html"
    model = all_cart
    success_url = reverse_lazy('cart')


def cart_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        price = int(request.POST['price'])
        photo = request.POST['photo']
        serial = request.POST['serial']
        cart_database = all_cart(username=username, name=name, price=price, photo=photo, serial=serial)
        cart_database.save()
        messages.success(request, "Added cart successfully.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_your_garden(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        price = int(request.POST['price'])
        photo = request.POST['photo']
        serial = request.POST['serial']
        category = request.POST['category']
        your_garden_database = your_garden(username=username, name=name, price=price, photo=photo, category=category, serial=serial)
        your_garden_database.save()
        messages.success(request, "Added your garden successfully.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def order_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['order_tree']
        order_id = request.POST['order_id']
        order_serial = request.POST['order_serial']
        number = request.POST['number']
        transaction_id = request.POST['transaction_id']
        order_form_database = order(username=username, name=name, order_id=order_id, order_serial=order_serial, number=number, transaction_id=transaction_id)
        order_form_database.save()
        messages.success(request, "Thank you.We have received your order.We will contact you soon.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class blog (ListView):
    template_name = "4_blog.html"
    model = all_blog
    ordering = ['-id']


class blog_details (DetailView):
    template_name = "blog_details.html"
    model = all_blog
    ordering = ['-id']


class portfolio (ListView):
    template_name = "3_portfolio.html"
    model = portfolio
    ordering = ['-id']


class make_your_garden (ListView):
    template_name = "make_your_garden.html"
    model = make_your_garden_yourself
    ordering = ['-id']


class make_your_garden_balcony (ListView):
    template_name = "make_your_garden_balcony.html"
    model = make_your_garden_yourself
    ordering = ['-id']


class make_your_garden_corporate (ListView):
    template_name = "make_your_garden_corporate.html"
    model = make_your_garden_yourself
    ordering = ['-id']



class my_garden (ListView):
    template_name = "your_garden.html"
    model = your_garden
    ordering = ['-id']

class about (ListView):
    template_name = "2_about-us.html"
    model = about


class payment (DetailView):
    template_name = "payment.html"
    model = all_cart

class payment_all (ListView):
    template_name = "11_payment-method.html"
    model = all_cart

    def get_context_data(self, **kwargs):
        context = super(payment_all, self).get_context_data(**kwargs)
        context['total_price'] = all_cart.objects.filter(username = self.request.user.username).aggregate(sum_all=Sum('price')).get('sum_all')
        return context



    
 
    




