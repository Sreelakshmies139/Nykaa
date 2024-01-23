from django.shortcuts import render, redirect
from NykaaBackend.models import CategoryDB, ProductDB
from NykaaFrontend.models import ContactDB, RegisterDB, CartDB, CheckoutDB
from django.contrib import messages


# Create your views here.
def home_page(req):
    cat = CategoryDB.objects.all()
    data = CartDB.objects.filter(Username=req.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(req, "Home.html", {'cat': cat, 'data': data, 'x': x})

def all_products(req):
    pro = ProductDB.objects.all()
    data = CartDB.objects.filter(Username=req.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(req, "AllProducts.html", {'pro': pro, 'data': data, 'x': x})

def products_page(req, cat_name):
    data = ProductDB.objects.filter(Category=cat_name)
    data1 = CartDB.objects.filter(Username=req.session['Name'])
    x = 0
    for i in data1:
        x = x + i.Quantity
    return render(req, "Products.html", {'data': data, 'data1': data1, 'x': x})

def contact_page(request):
    data = CartDB.objects.filter(Username=request.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(request, "Contact.html", {'data': data, 'x': x})

def save_contact(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('subject')
        m = request.POST.get('message')
        obj = ContactDB(Name=n, Email=e, Subject=s, Message=m)
        obj.save()
        messages.success(request, "Enquiry Successful")
        return redirect(contact_page)

def about_page(request):
    data = CartDB.objects.filter(Username=request.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(request, "About.html", {'data': data, 'x': x})

def single_product(request, pro_id):
    pro = ProductDB.objects.get(id=pro_id)
    data = CartDB.objects.filter(Username=request.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(request, "SingleProduct.html", {'pro': pro, 'data': data, 'x': x})

def user_reg(request):
    return render(request, "UserRegistration.html")

def user_login(request):
    return render(request, "UserLogin.html")

def save_user(request):
    if request.method == "POST":
        n = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('pass1')
        c = request.POST.get('pass2')
        i = request.FILES['image']
        obj = RegisterDB(Name=n, Email=e, Password=p, ConfirmPassword=c, Image=i)
        obj.save()
        messages.success(request, "User Registered Successfully...!")
        return redirect(user_login)

def login_user(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if RegisterDB.objects.filter(Name=un, Password=pwd).exists():
            request.session['Name'] = un
            request.session['Password'] = pwd
            messages.success(request, "User Logged In Successfully...!")
            return redirect(home_page)
        else:
            return redirect(user_login)
    else:
        return redirect(user_login)

def logout_user(request):
    del request.session['Name']
    del request.session['Password']
    messages.error(request, "User Logged Out Successfully")
    return redirect(user_login)


def display_user(req, userid):
    data = RegisterDB.objects.get(id=userid)
    return render(req, "DisplayUser.html", {'data': data})


def save_cart(request):
    if request.method == "POST":
        use = request.POST.get('uname')
        pro = request.POST.get('pro_name')
        qua = request.POST.get('quantity')
        pri = request.POST.get('price')
        tot = request.POST.get('total_price')
        obj = CartDB(Username=use, Pro_Name=pro, Quantity=qua, Price=pri, Total_Price=tot)
        obj.save()
        messages.success(request, "Product Successfully Added To Cart...!")
        return redirect(home_page)

def cart_page(request):
    data = CartDB.objects.filter(Username=request.session['Name'])
    grand_total = 0
    x = 0
    for i in data:
        x = x + i.Quantity
    for d in data:
        grand_total = grand_total + d.Total_Price
    return render(request, "Cart.html", {'data': data, 'grand_total': grand_total, 'x': x})


def delete_cart_item(req, cartid):
    x = CartDB.objects.filter(id=cartid)
    x.delete()
    messages.error(req, "Product Deleted From Cart")
    return redirect(cart_page)

def checkout_page(request):
    data = CartDB.objects.filter(Username=request.session['Name'])
    grand_total = 0
    x = 0
    for i in data:
        x = x + i.Quantity
    for d in data:
        grand_total = grand_total + d.Total_Price
    return render(request, "Checkout.html", {'data': data, 'grand_total': grand_total, 'x': x})

def save_checkout(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        ci = request.POST.get('city')
        co = request.POST.get('country')
        pi = request.POST.get('pincode')
        mo = request.POST.get('mobile')
        obj = CheckoutDB(Name=na, Email=em, Address=ad, City=ci, Country=co, Pincode=pi, Mobile=mo)
        obj.save()
        messages.success(request, "Order Placed Successful...!")
        return redirect(home_page)

