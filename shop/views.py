from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ReviewForm

from .models import Product, Category
# Create your views here.

# http://127.0.0.1:8000/
def product_list(request, slug=None):
    products = Product.objects.filter(available=True)
    # http://127.0.0.1:8000/category/elektronika
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)

    context = {'products': products, 'categories': categories}
    return render(request, 'product_list.html', context)

# http://127.0.0.1:8000/product/mylo
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    reviews = product.reviews.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.save()
            return redirect('product_detail', slug=product.slug)
        
    context = {'product': product, 'form': form, 'reviews': reviews}
    return render(request, 'product_detail.html', context)
