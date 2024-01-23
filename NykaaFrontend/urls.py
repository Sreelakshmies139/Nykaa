from django.urls import path
from NykaaFrontend import views

urlpatterns = [
    path('home_page/', views.home_page, name="home_page"),
    path('all_products/', views.all_products, name="all_products"),
    path('products_page/<cat_name>/', views.products_page, name="products_page"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('about_page/', views.about_page, name="about_page"),
    path('single_product/<int:pro_id>/', views.single_product, name="single_product"),
    path('user_reg/', views.user_reg, name="user_reg"),
    path('user_login/', views.user_login, name="user_login"),
    path('save_user/', views.save_user, name="save_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('display_user/<int:userid>/', views.display_user, name="display_user"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('delete_cart_item/<int:cartid>/', views.delete_cart_item, name="delete_cart_item"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('save_checkout/', views.save_checkout, name="save_checkout")
]
