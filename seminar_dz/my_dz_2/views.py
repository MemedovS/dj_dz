

from django.shortcuts import render
from .models import Client, Product, Order

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'my_dz_2/client_detail.html', {'client': client, 'orders': orders})