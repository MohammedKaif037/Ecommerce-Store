from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from StoreApp.forms import UserForm
from StoreApp.models import Category, products
from .forms import ShippingInformationForm, PaymentInformationForm
from xhtml2pdf import pisa
# Create your views here.

def index_function(request):
    all_products=products.objects.filter(pid_for_home=1)
    return render(request, 'StoreApp/index.html', {'products': all_products})

def shop_function(request):
    return render(request, 'StoreApp/shop.html')

def aboutus_function(request):
    return render(request, 'StoreApp/about.html')

def categories_function(request):
    return render(request, 'StoreApp/categories.html')

def contactus_function(request):
    form=UserForm()
    return render(request, 'StoreApp/contactus.html',{'form': form})

def electronics_function(request):
    category_id=Category.objects.get(title='Electronics').id
    electronics_products=products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html',{'electronics_products':electronics_products})
def fashion_function(request):
    category_id = Category.objects.get(title='Fashion').id
    fashion_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'fashion_products': fashion_products})

def home_and_decorations_function(request):
    category_id = Category.objects.get(title='Home and Garden').id
    home_and_decor_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'home_and_decor_products': home_and_decor_products})

def toys_and_games_function(request):
    category_id = Category.objects.get(title='Toys and Games').id
    toys_and_games_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'toys_and_games_products': toys_and_games_products})

def sports_and_fitness_function(request):
    category_id = Category.objects.get(title='Sports and Fitness').id
    sports_and_fitness_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'sports_and_fitness_products': sports_and_fitness_products})

def skincare_function(request):
    category_id = Category.objects.get(title='Skincare and cosmetics').id
    skincare_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'skincare_products': skincare_products})



def storeuserdata_function(request):
    user_form=UserForm()
    if request.method == 'POST':
        user_data=UserForm(request.POST)
        user_data_instance=user_data.instance
        if user_data.is_valid():
            user_data.save()
            return render(request, 'StoreApp/contactus.html', {'user_data': user_data_instance})
    context={'form': user_form}
    return render(request, 'StoreApp/contactus.html', context=context)

# def checkout_function(request):
#     title = request.GET.get('title', None)
#     price = request.GET.get('price', None)
#     if request.method == 'POST':
#         shipping_form = ShippingInformationForm(request.POST)
#         payment_form = PaymentInformationForm(request.POST)
#         if shipping_form.is_valid() and payment_form.is_valid():
#             shipping_info = shipping_form.save()
#             payment_info = payment_form.save(commit=False)
#             payment_info.shipping_information = shipping_info
#             payment_info.save()
#             return redirect('success_page')  # Redirect to a success page
#     else:
#         # title = request.GET.get('title','None') will act as local and throw UnboundLocalError at /checkout/
#         # price = request.GET.get('price','None') will act as local and throw UnboundLocalError at /checkout/
#         shipping_form = ShippingInformationForm()
#         payment_form = PaymentInformationForm()
#     return render(request, 'StoreApp/checkout.html', {'shipping_form': shipping_form, 'payment_form': payment_form,'title': title, 'price':price})

# @csrf_exempt
# def checkout_function(request):
#     print('Checkout function called')
#     title = request.GET.get('title', None)
#     price = request.GET.get('price', None)
#     print('title: %s, price: %s' % (title, price))
#     if request.method == 'POST':
#         print('POST request received')
#         shipping_form = ShippingInformationForm(request.POST)
#         payment_form = PaymentInformationForm(request.POST)
#         print(shipping_form,payment_form)
#         if shipping_form.is_valid() and payment_form.is_valid():
#             shipping_info = shipping_form.save()
#             payment_info = payment_form.save(commit=False)
#             payment_info.shipping_information = shipping_info
#             payment_info.save()
#             return redirect('success')  # Redirect to a success page
#     else:
#         shipping_form = ShippingInformationForm()
#         payment_form = PaymentInformationForm()
#     return render(request, 'StoreApp/checkout.html', {'shipping_form': shipping_form, 'payment_form': payment_form, 'title': title, 'price': price})


# def invoice_function(request):
#     if request.method == 'POST':
#         # Process form data
#         title = request.POST.get('title')
#         price = request.POST.get('price')
#         shipping_details = request.POST.get('shipping_details')
#         payment_info = request.POST.get('payment_info')
        
#         # Pass data to the invoice template
#         template_path = 'success.html'
#         context = {'title': title, 'price': price, 'shipping_details': shipping_details, 'payment_info': payment_info}
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'filename="invoice.pdf"'
#         template = get_template(template_path)
#         html = template.render(context)

#         # Create PDF
#         pisa_status = pisa.CreatePDF(html, dest=response)
#         if pisa_status.err:
#             return HttpResponse('We had some errors <pre>' + html + '</pre>')
#         return response
#     else:
#         return HttpResponse("Method Not Allowed")
@csrf_exempt
def checkout_function(request):
    print('Checkout function called')
    title = request.GET.get('title', None)
    price = request.GET.get('price', None)
    print('title: %s, price: %s' % (title, price))

    if request.method == 'POST':
        print('POST request received')
        shipping_form = ShippingInformationForm(request.POST)
        payment_form = PaymentInformationForm(request.POST)
        print(shipping_form, payment_form)

        if shipping_form.is_valid() and payment_form.is_valid():
            shipping_info = shipping_form.save()
            payment_info = payment_form.save(commit=False)
            payment_info.shipping_information = shipping_info
            payment_info.save()

            # Pass data to the invoice template
            template_path = 'StoreApp/Success.html'
            context = {'title': title,
                       'price': price,
                       'shipping_details': {
                           'full_name': shipping_info.full_name,
                           'address': shipping_info.address,
                           'city': shipping_info.city,
                           'state_province': shipping_info.state_province,
                           'postal_code': shipping_info.postal_code,
                           'country': shipping_info.country,
                       },
                       'payment_info': {
                           'card_number': payment_info.card_number,
                           'expiration_date': payment_info.expiration_date,
                           'cvv': payment_info.cvv,
                           'billing_address': payment_info.billing_address,
                       }
            }
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="invoice.pdf"'
            template = get_template(template_path)
            html = template.render(context)

            # Create PDF
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
    else:
        shipping_form = ShippingInformationForm()
        payment_form = PaymentInformationForm()

    return render(request, 'StoreApp/checkout.html', {'shipping_form': shipping_form, 'payment_form': payment_form, 'title': title, 'price': price})
def success_page_function(request):
    return render(request, 'StoreApp/Success.html')
