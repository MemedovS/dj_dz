
from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('registration_date',)

admin.site.register(Client, ClientAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_date')
    search_fields = ('name',)
    list_filter = ('added_date', 'price')
    readonly_fields = ('added_date',)

    def product_price(self, obj):
        return f"${obj.price}"


admin.site.register(Product, ProductAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('client__name', 'client__email')
    list_filter = ('order_date', 'total_amount')
    filter_horizontal = ('products',)
    readonly_fields = ('total_amount', 'order_date')

    def total_amount_display(self, obj):
        return f"${obj.total_amount}"


admin.site.register(Order, OrderAdmin)
