from django.shortcuts import render , HttpResponseRedirect
from home.models import Candels,ResignArt,Order
from django.core.mail import send_mail

def home(request):
    data = {
        "title" : "Home",
    }

    return render(request,'index.html',data)

def billingAddress(request,id):
    if request.method == 'POST':
            product_name = id
            f_name = request.POST.get('first_name')
            l_name = request.POST.get('last_name')
            cust_email = request.POST.get('customer_email')
            phone = request.POST.get('phone_number')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            # shiping_country = request.POST.get('country')
            shiping_state = request.POST.get('state')
            shiping_dist = request.POST.get('district')
            shiping_town = request.POST.get('city/town')
            number_of_order = request.POST.get('quantity')
            shiping_zip = request.POST.get('zip_code')

            order = Order(product_name,
                          first_name=f_name,
                          last_name=l_name,
                          email=cust_email,
                          phone_number=phone,
                          address_1=address1,
                          address_2=address2,
                        #   country=shiping_country,
                          state=shiping_state,
                          district=shiping_dist,
                          town=shiping_town,
                          quantity=number_of_order,
                          zip_code=shiping_zip,
                          payment_done=False,
                          )
            order.save()
            return HttpResponseRedirect("/payment/")
    data={
        'title': 'Billing',
        'ID':id,
        'confirm' : False,
        'message' : 'Order Was Confirmed!'
    }
    return render(request,'Billing.html',data)

def candleDetails(request,id):
    Data = Candels.objects.get(id=id)
    # print(Data)
    data = {
        'Data':Data,
        "title" : "Candle Detail",
    }
    return render(request,'Check_Out_Candles.html',data)

def resinArtDetails(request,id):
    Data = ResignArt.objects.get(id=id)
    # print(Data)
    data = {
        'Data':Data,
        "title" : "Resign Detail",
    }
    return render(request,'Check_Out_ResinArt.html',data)

def payment(request):
    data={
        'title':'Payment',
    }
    return render(request,"Payment.html",data)

def about(request):
    data = {
        "title" : "About",
    }
    return render(request,'About.html',data)

def new_genart(request):
    Data = ResignArt.objects.all()
    data = {
        "title" : "Resin Art",
        "Data":Data,
    }
    return render(request,'New_Genart.html',data)

def new_candels(request):
    Data = Candels.objects.all()
    data = {
        "title" : "Candels",
        "Data" : Data,
    }
    return render(request,'New_Candels.html',data)

def contact(request):
    data = {
        "title" : "Contact",
    }
    return render(request,'Contact.html',data)
