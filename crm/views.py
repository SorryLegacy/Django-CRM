from django.shortcuts import render


from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from telebot.sendmessage import send_telegram


def first_page(request):
    """Main page with all models"""
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {
            'slider_list': slider_list,
            'pc_1': pc_1,
            'pc_2': pc_2,
            'pc_3': pc_3,
            'price_table': price_table,
            'form': form,
        }

    return render(request, './index.html', dict_obj)


def thanks_page(request):
    """Thanks page for customer who leave order"""
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(name, phone)
        return render(request, './thanks.html',
                      {
                          'name': name,
                          'phone': phone,
                      })
    else:
        return render(request, './thanks.html', '')
# Create your views here.
