
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('repair', views.repair,name="repair"),

    path('ram/', views.ram,name="ram"),
    path('contact', views.contact,name="contact"),
    path('order', views.order,name="order"),
    path('service', views.service,name="service"),
    path('gas', views.gas,name="gas"),
    path('send-order/', views.send_order_whatsapp, name="send_order_whatsapp"),
    path('login', views.login,name="login"),
    path('', views.welcom,name="welcom"),
    path('ragister', views.ragister,name="ragister"),
]
