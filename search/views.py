from django.shortcuts import render
from products.models import Product
from search.documents import ProdDocument

# Create your views here.


def do_search(request):
    #products = Product.objects.filter(name__icontains=request.GET['q'])
    q = request.GET.get('q')
    if q:
    	products = ProdDocument.search().query("match", name=q)
    else:
    	products = ''
    return render(request, "search.html", {"products": products})