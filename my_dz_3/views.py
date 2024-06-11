# views.py
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Order

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'my_dz_3/client_detail.html', {'client': client, 'orders': orders})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'my_dz_3/client_list.html', {'clients': clients})
def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    now = timezone.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)
    year_ago = now - timedelta(days=365)

    orders_week = Order.objects.filter(client=client, order_date__gte=week_ago)
    orders_month = Order.objects.filter(client=client, order_date__gte=month_ago)
    orders_year = Order.objects.filter(client=client, order_date__gte=year_ago)

    products_week = {product for order in orders_week for product in order.products.all()}
    products_month = {product for order in orders_month for product in order.products.all()}
    products_year = {product for order in orders_year for product in order.products.all()}

    context = {
        'client': client,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, 'my_dz_3/client_orders.html', context)




