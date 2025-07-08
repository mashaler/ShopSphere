from django.shortcuts import render, HttpResponse, redirect
from .models import Allproducts, profile, Comment, Order
from django.contrib.auth.models import User
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    cats = Allproducts.objects.values("prod_category")
    print(cats)
    cat = {item["prod_category"] for item in cats}
    # all = Allproducts.objects.filter(prod_category= "hoodies")[0:9]
    all = Allproducts.objects.all().order_by("?")[0:9]
    asc = Allproducts.objects.filter(prod_category= "hoodies").order_by("prod_price")[0:9]
    desc = Allproducts.objects.filter(prod_category= "hoodies").order_by("-prod_price")[0:9]
    new_arrival = Allproducts.objects.all().order_by("?")[0:9]
    trending = Allproducts.objects.all().order_by("-prod_view")[0:3]
    pr= request.POST.get("sort")
    if pr== "asc":
        all_prod  = asc
    elif pr == "desc":
        all_prod = desc
    else:
        all_prod = all
    parameters = {
        "all" : all_prod,
        "cat": cat,
        "new" : new_arrival,
        "trending" : trending
    }
    # subject = 'welcome to R fashion'
    # message = f'Hi thank you for choosing us.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ["ravisinghd98@gmail.com", ]
    # send_mail( subject, message, email_from, recipient_list )
    
    return render(request, "index.html" , parameters)

def categories(request, cat):
     cats = Allproducts.objects.values("prod_category")
     category = {item["prod_category"] for item in cats}
     all = Allproducts.objects.filter(prod_category= cat)
     asc = Allproducts.objects.filter(prod_category= cat).order_by("prod_price")[0:9]
     desc = Allproducts.objects.filter(prod_category= cat).order_by("-prod_price")[0:9]
     pr= request.POST.get("sort")
     if pr== "asc":
         all_prod  = asc
     elif pr == "desc":
         all_prod = desc
     else:
         all_prod = all
     params = {
        "all" : all_prod,
        "cat": category

    }
     return render(request, "categories.html", params)



def detailpage(request, slug):
    detail_prod = Allproducts.objects.get(prod_slug = slug)
    detail_prod.prod_view += 1
    detail_prod.save()

# REALTED PRODUCTS QUERY 

    related_products = Allproducts.objects.filter(prod_category = detail_prod.prod_category).exclude(prod_id = detail_prod.prod_id)

    if request.method == "POST":
        if request.user.is_authenticated:
            comment_contents = request.POST.get("feedback")
            rating = request.POST.get("rating-no")
            comment = Comment(prod_rating = rating, comment_post = detail_prod, comment_content = comment_contents, comment_user = request.user, )
            comment.save()
            return redirect(f"/detailpro/{detail_prod.prod_slug}")
        else:
            return redirect("/signin")
    
    comnt_detail= Comment.objects.filter(comment_post = detail_prod)

    params = {
        "detail" : detail_prod,
        "comment" : comnt_detail,
        "all" : related_products
    }
    return render(request, "productpage.html", params)

#Creating A Client For Payment
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))


#Order Suucess page after successfuly order of any products
def showOrderPage(request):
    if request.method == "POST":
        prod = request.POST.get("product")
        prodColor = request.POST.get("color")
        prodSize = request.POST.get("size")
        prodPrice = request.POST.get("price")
        prdQuantity = request.POST.get("prod_quantity")

        instanceProd = Allproducts.objects.get(prod_id = prod)
        order_amount = int(prodPrice) * 100
        order_currency = "INR"
        order_recipt  = "order_rcptid_11"

        razorpay_order = razorpay_client.order.create(dict(
            amount = order_amount,
            currency = order_currency,
            receipt = order_recipt,
            payment_capture = 1,
        ))

        order_id = razorpay_order["id"]
        context = {
            "product" : instanceProd,
            "order_id" : order_id,
            "amount" : order_amount,
            "display_amount" : prodPrice,
            "currency" : order_currency,
            "api_key" : settings.RAZORPAY_API_KEY,
        }
        
        return render(request, "orderSuccess.html", context)
    return render(request, "index.html")


#checking Payment Succsess
@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            order_id = request.POST.get("razorpay_order_id", "")
            signature = request.POST.get("razorpay_signature", "")

            context={
               "razorpay_order_id" : order_id,
               "razorpay_payment_id" : payment_id,
               "razorpay_signature" : signature
            }
            result = razorpay_client.utility.verify_payment_signature(context)

            if result:
                return render(request, "paymentSuccess.html")
            else:
                return render(request, "paymentFailed.html")
        except:
                return render(request, "paymentFailed.html")
    else:
        return render(request, "paymentFailed.html")




def showCart(request):
    return render(request, "cart.html")

def check(value, allprod):
    if((value in (allprod.prod_name).lower()) or (value in (allprod.prod_desc).lower())):
        return True
    else:
        return False


def search(request):
    search_prod = []
    allprod = Allproducts.objects.all()
    if request.method == "GET":
        value = request.GET.get("search").lower()
        for item in allprod:
            if check(value, item):
                search_prod.append(item)
            else:
                pass

        return render(request, "search_product.html", {"allprod" : search_prod} )
    return render(request, "index.html")

def signin(request):
    if request.method == "POST":
        usename = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username= usename, password= password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("invalid")

    return render(request, "signin.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone= request.POST.get("phone")
        add1= request.POST.get("add1")
        add2 = request.POST.get("add2")
        pincode = request.POST.get("pincode")

        user = User.objects.create_user(email, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        profile_detail = profile(user_detail= user, user_addres= add1, user_landnark= add2, user_phone= phone, user_pincode= pincode)
        profile_detail.save()
        return redirect("/signin")
    return render(request, "signup.html")

def logout_user(request):
    logout(request)
    return redirect("/")