"""RetailShopIITI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
from shopapp.views import main_page, cart, wishlist, wishlist_product, main_page_product, main_page_cart_product, orders, main_page_order_product, aboutus, main_page_electronics, main_page_stationary, main_page_household, main_page_fashion, profile
from Retailer.views import mainpage, update_product, add_product_form, add_product, update_product_form, delete_product, retailer_profile, retailer_orders, retailer_orders_product
from django.urls import include
from payments.views import initiate_payment, proceed_payment, cart_initiate_payment, cart_proceed_payment, cartall_initiate_payment, cartall_proceed_payment

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-in/', views.homeview),
    path('sign-in/signupauth/', views.signupauth),
    path('sign-in/login/', views.login),
    path('sign-in/Re_login/', views.relogin),
    path('', views.welcome),
    path('home/', views.openview),
    path('resetpassword/', views.forgetview),
    path('ticket/', views.ticket, name='ticket'),
    path('main-page/', main_page),
    path('main-page/<int:id>/pay/', initiate_payment),
    path('main-page/cart/<int:id>/pay/', cart_initiate_payment),
    path('main-page/cartall/pay/', cartall_initiate_payment),
    path('main-page/<int:id>/pay/proceed/', proceed_payment),
    path('main-page/cart/<int:id>/pay/proceed/', cart_proceed_payment),
    path('main-page/cartall/pay/proceed/', cartall_proceed_payment),
    path('main-page/electronics/', main_page_electronics),
    path('main-page/stationary/', main_page_stationary),
    path('main-page/household/', main_page_household),
    path('main-page/fashion/', main_page_fashion),
    path('main-page/<int:id>/', main_page_product),
    path('main-page/cart/<int:id>/', main_page_cart_product),
    path('main-page/orders/<int:id>/', main_page_order_product),
    path('main-page/cart/', cart),
    path('main-page/wishlist/', wishlist),
    path('main-page/wishlist/<int:id>/', wishlist_product),
    path('main-page/orders/', orders),
    path('Retailer/', mainpage),
    path('Retailer/add/', add_product_form),
    path('Retailer/add/a/', add_product),
    path('Retailer/update/', update_product_form),
    path('Retailer/update/u/', update_product),
    path('Retailer/delete/', delete_product),
    path('main-page/profile/', profile),
    path('Retailer/Profile/', retailer_profile),
    path('Retailer/orders/', retailer_orders),
    path('Retailer/orders/<int:id>/', retailer_orders_product),
    path('main-page/aboutUs/', aboutus),
    path('', include('payments.urls')),



#     url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
#     url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
