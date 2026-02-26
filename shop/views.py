from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserRegister

from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from django.http import JsonResponse
from urllib.parse import quote

# Create your views here.
def index(request):
    return render(request,'shop/home.html')

def about(request):
    #return render(request,'shop/index.html')
    return render(request,'shop/about.html')
    

def ram(request):
   return render(request,'shop/electrician.html')
   #return HttpResponse("if u have any trouble than contact me ")
    
def contact(request):
   return render(request,'shop/contact.html')

def order(request):
   return render(request,'shop/order.html')

def service(request):
   return render(request,'shop/card2.html')
def gas(request):
   return render(request,'shop/gas.html')
def repair(request):
   return render(request,'shop/repair.html')


def welcom(request):
   return render(request,'shop/index.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserRegister.objects.get(email=email)

            if check_password(password, user.password):
                request.session["user_id"] = user.id
                request.session["user_email"] = user.email
                return redirect("index")  # make sure URL name exists
            else:
                messages.error(request, "Invalid email or password")

        except UserRegister.DoesNotExist:
            messages.error(request, "Invalid email or password")

    return render(request, "shop/login.html")

def ragister(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect("ragister")

        if UserRegister.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("ragister")

        UserRegister.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "shop/ragister.html")

from django.http import JsonResponse
from urllib.parse import quote

def send_order_whatsapp(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        notes = request.POST.get("notes")
        service = request.POST.get("service")

        whatsapp_number = "918286489848"  # Admin WhatsApp number

        message = f"""
📦 *NEW ORDER RECEIVED*

🛠 Service: {service}

👤 Customer Name: {name}
📞 Phone: {phone}
📧 Email: {email}

🏠 Address / Notes:
{notes}

✅ Order Status: CONFIRMED
"""

        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={quote(message)}"

        return JsonResponse({
            "status": "success",
            "whatsapp_url": whatsapp_url
        })

    return JsonResponse({"status": "error"})