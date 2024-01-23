from django.shortcuts import render, redirect
from NykaaBackend.models import CategoryDB
from NykaaBackend.models import ProductDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from NykaaFrontend.models import ContactDB
from django.contrib import messages

# Create your views here.
def index_page(req):
    return render(req, "index.html")

def category_page(request):
    return render(request, "Category.html")

def category_save_data(request):
    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('description')
        i = request.FILES['image']
        obj = CategoryDB(Name=n, Description=d, Image=i)
        obj.save()
        messages.success(request, "Category Added Successfully...!")
        return redirect(category_page)

def display_category(request):
    data = CategoryDB.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})

def edit_category(req, categoryid):
    data = CategoryDB.objects.get(id=categoryid)
    return render(req, "EditCategory.html", {'data': data})

def update_category(req, categoryid):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('description')
        try:
            pr = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(pr.name, pr)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=categoryid).Image
        CategoryDB.objects.filter(id=categoryid).update(Name=na, Description=de, Image=file)
        messages.success(req, "Category Edited Successfully...!")
        return redirect(display_category)

def delete_category(req,categoryid):
    x = CategoryDB.objects.filter(id=categoryid)
    x.delete()
    messages.error(req, "Category Deleted Successfully...!")
    return redirect(display_category)

def product_page(request):
    cat = CategoryDB.objects.all()
    return render(request, "Product.html", {'cat': cat})

def product_save_data(request):
    if request.method == "POST":
        ca = request.POST.get('category')
        na = request.POST.get('name')
        sp = request.POST.get('specification')
        mr = request.POST.get('price')
        im1 = request.FILES['image1']
        im2 = request.FILES['image2']
        im3 = request.FILES['image3']
        obj1 = ProductDB(Category=ca, Name=na, Specification=sp, Price=mr, Image1=im1, Image2=im2, Image3=im3)
        obj1.save()
        messages.success(request, "Product Added Successfully...!")
        return redirect(product_page)

def display_product(request):
    data1 = ProductDB.objects.all()
    return render(request, "DisplayProduct.html", {'data1': data1})


def edit_product(req, productid):
    cat = CategoryDB.objects.all()
    data1 = ProductDB.objects.get(id=productid)
    return render(req, "EditProduct.html", {'data1': data1, 'cat': cat})


def update_product(req, productid):
    if req.method == "POST":
        ca = req.POST.get('category')
        na = req.POST.get('name')
        sp = req.POST.get('specification')
        mr = req.POST.get('price')
        try:
            im1 = req.FILES['image1']
            fs1 = FileSystemStorage()
            file1 = fs1.save(im1.name, im1)
        except MultiValueDictKeyError:
            file1 = ProductDB.objects.get(id=productid).Image1

        try:
            im2 = req.FILES['image2']
            fs2 = FileSystemStorage()
            file2 = fs2.save(im2.name, im2)
        except MultiValueDictKeyError:
            file2 = ProductDB.objects.get(id=productid).Image2

        try:
            im3 = req.FILES['image3']
            fs3 = FileSystemStorage()
            file3 = fs3.save(im3.name, im3)
        except MultiValueDictKeyError:
            file3 = ProductDB.objects.get(id=productid).Image3

        ProductDB.objects.filter(id=productid).update(Category=ca, Name=na, Specification=sp, Price=mr, Image1=file1, Image2=file2, Image3=file3)
        messages.success(req, "Product Edited Successfully...!")
        return redirect(display_product)


def delete_product(req, productid):
    x = ProductDB.objects.filter(id=productid)
    x.delete()
    messages.error(req, "Product Deleted Successfully...!")
    return redirect(display_product)

def login_page(req):
    return render(req, "AdminLogin.html")

def Admin_login(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('passwd')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "User Logged In Successfully...!")
                return redirect(index_page)
            else:
                messages.error(request, "Invalid Password")
                return redirect(login_page)
        else:
            messages.error(request, "Please check the Username...!")
            return redirect(login_page)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request, "User Logged Out Successfully")
    return redirect(login_page)

def contact_data(request):
    data = ContactDB.objects.all()
    return render(request, "Contact_Data.html", {'data': data})

def delete_contact(req, contactid):
    x = ContactDB.objects.filter(id=contactid)
    x.delete()
    return redirect(contact_data)