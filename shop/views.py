from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.
def index(request):
    text_var = 'this is not my first django web app'
    return HttpResponse(text_var)

def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    ''' Pagination Code'''
    paginator = Paginator(products_list, 2)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    context = {
        'category': c_page,
        'products': products,
    }
    return render(request, 'shop/category.html', context)

def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'product': product,
    }
    return render(request, 'shop/product.html', context)
