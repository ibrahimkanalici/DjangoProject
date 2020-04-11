from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'dayproducts': dayproducts}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category, }
    return render(request, 'hakkimizda.html', context)


def referanslarimiz(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category, }
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':  # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kur
            data.name = form.cleaned_data['name']  # formdan bilgi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,
               'form': form,
               'category': category}
    return render(request, 'iletisim.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               'slug': slug,
               'categorydata': categorydata
               }
    return render(request, 'products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    productdata = Product.objects.get(pk=id)
    setting = Setting.objects.get(pk=1)
    images = Images.objects.filter(product_id = id)
    context = {  # 'product': product,
                    'category': category,
                     'setting': setting,
                        'images': images,
                     'productdata': productdata}
    return render(request, 'product_detail.html', context)
