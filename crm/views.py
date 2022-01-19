from django.shortcuts import render


from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from telebot.sendmessage import send_telegram



def first_page(requset):
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

    return render(requset, './index.html', dict_obj)


def thanks_page(requset):
    if requset.POST:
        name = requset.POST['name']
        phone = requset.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(name, phone)
        return render(requset, './thanks.html',
                      {
                          'name': name,
                          'phone': phone,
                      })
    else:
        return render(requset, './thanks.html', '')
# Create your views here.
