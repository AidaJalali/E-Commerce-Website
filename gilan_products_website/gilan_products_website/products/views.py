from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from decimal import Decimal

from .forms import CustomUserCreationForm
from .models import CustomUser, Category, Product, Order, OrderItem


#1) Auth Views
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()  
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('product_list')
    return render(request, 'logout.html')



#2) Product views

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    #search by name
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)

    #filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        'products':products,
        'categories':categories,
    }

    return render(request, 'product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

'''
@login_required
def product_create(request):
    #only authenticated users can create new products
    if request.method == 'POST':
        form = ProductForm(request.Post, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})
'''



#3) Cart and Order views

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    #increament product quantity in cart
    cart[str(product_id)] = cart.get(str(product_id),0) + 1
    request.session['cart'] = cart
    return redirect('cart_view')


def cart_view(request):
    cart = request.session.get('cart',{})
    cart_items = []
    total = Decimal('0.00')

    for pid_str, qty in cart.items():
        product = Product.objects.get(id=pid_str)
        qty = int(qty)
        item_total = product.price * qty
        cart_items.append({
            'product': product,
            'quantity': qty,
            'item_total': item_total
        })
        total += item_total

    return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total' : total,
        })


@login_required
def checkout(request):
    cart = request.session.get('cart',{})
    if not cart:
        return redirect('cart_view')
    

    #create new order
    order = Order.objects.create(user=request.user)
    for pid_str, qty in cart.items():
        product = Product.objects.get(id=pid_str)
        qty = int(qty)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
            price=product.price
        )
    request.session['cart'] = {}

    return render(request, 'checkout_success.html', {'order':order})

