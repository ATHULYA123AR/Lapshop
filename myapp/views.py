from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import logout
from myapp.models import  laptop,accessories,Signuptable,newproducts,Carttable,Billtable,Contact
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from decimal import Decimal
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request,"index.html")





def shop1(request):
    return render(request,"shop1.html")



def shop1_products(request):
    a = laptop.objects.all()
    return render(request, "shop1.html", {"cardkeys": a})


def productinfo(request,id1):
    p = laptop.objects.filter(id=id1).first()
    return render(request, 'productonly.html', {'prokeys': p})






def shop2(request):
    return render(request,"shop2.html")



def shop2_products(request):
    a = accessories.objects.all()
    return render(request, "shop2.html", {"cardkeyss": a})



def productinfos(request, id1):
    p = get_object_or_404(accessories, id=id1)
    return render(request, 'productonly1.html', {'prokeyss': p})


def signup(request):
    if request.method == 'POST':
        a = request.POST['name1']
        b = request.POST['name2']
        c = request.POST['name3']
        d = request.POST['name4']
        e = request.POST['name5']
        f = request.POST['name6']
        g = request.POST['name7']

        if User.objects.filter(username=f).exists():
            messages.error(request, "Username already exists.")
            return render(request, "signup.html")

        try:
            # Create the user
            user = User.objects.create_user(username=f, password=g)
            user.save()

            # Create the Signup entry
            e = Signuptable(first_name=a, last_name=b, mobile=c, email=d, place=e, username=f, password=g, user=user)
            e.save()

        except IntegrityError:
            messages.error(request, "An error occurred. Please try again.")
            messages.error(request, "An error occurred. Please try again.")
            messages.error(request, "An error occurred. Please try again.")

            return render(request, "signup.html")
        return redirect('signin')
    return render(request, 'signup.html')





def signin(request):
    if request.method == 'POST':
        a = request.POST['name1']
        b = request.POST['name2']
        user = authenticate(username=a, password=b)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid username or password')
    return render(request, "signin.html")



def about(request):
    return render(request,"about.html")



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(newproducts, id=product_id)

    if request.method == "POST":
        try:
            quantity = int(request.POST.get("quantity"))
            if quantity <= 0:
                return HttpResponseBadRequest("Quantity must be a positive integer.")

            unit_price = product.Price
            image = product.Image
            total_price = quantity * unit_price

            # Save to Carttable
            cart_entry = Carttable(
                product_id=product.id,
                product_name=product.ProductName,
                quantity=quantity,
                image=image,
                total_price=total_price,
                user_id=request.user.id
            )
            cart_entry.save()

            return redirect('cart')

        except ValueError:
            return HttpResponseBadRequest("Invalid quantity.")
        except Exception as e:
            return HttpResponseBadRequest(f"An error occurred: {e}")

@login_required
def cart(request):
    cart_items = Carttable.objects.filter(user_id=request.user.id)

    grand_total = sum(item.total_price for item in cart_items)

    return render(request, "cart.html", {"cartkey": cart_items,"grand_total": grand_total})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Carttable, id=item_id)
    cart_item.delete()
    return redirect('cart')





def lout(request):
    logout(request)
    return redirect('home')




@login_required
def checkout(request):
    user_id = request.user.id
    cart_items = Carttable.objects.filter(user_id=user_id)

    sub_total = sum(Decimal(item.total_price) * item.quantity for item in cart_items)
    tax = sub_total * Decimal('0.001')  # Assuming 10% tax rate
    shipping_cost = Decimal('50')  # Assuming a flat shipping rate
    grand_total = sub_total + tax + shipping_cost

    if request.method == 'POST':
        # Retrieve form data safely
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')

        if all([first_name, last_name, mobile, email, address, country, state, zip_code]):
            for item in cart_items:
                Billtable.objects.create(
                    # Using product_name from cart_items
                    product_name=item.product_name,
                    first_name=first_name,
                    last_name=last_name,
                    mobile=mobile,
                    email=email,
                    quantity=item.quantity,
                    total_price=item.total_price * item.quantity,
                    user_id=request.user.id
                )

            cart_items.delete()

            return render(request, 'order_success.html')
        else:
            print("Form data missing")

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'tax': tax,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,
    }

    return render(request, 'checkout.html', context)
@login_required
def order_success(request):
    return render(request, 'order_success.html')



@login_required
def show_bill(request):
    user_id = request.user.id
    bills = Billtable.objects.filter(user_id=user_id)
    context = {
        'bills': bills,
    }
    return render(request, 'show_bill.html', context)



def contact_success(request):
    return render(request,"contact_success.html")





def contacts(request):
    if request.method == "POST":
        n1 = request.POST['name1']
        n2 = request.POST['name2']
        n3 = request.POST['name3']
        n4 = Contact(name=n1, email=n2, message=n3)
        n4.save()
        return render(request, "contact_success.html")  # Ensure this template exists
    return render(request, "contact_us.html")