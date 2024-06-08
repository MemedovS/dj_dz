from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('random_roll', views.random_roll, name='random_roll'),
    # path('random_number', views.random_number, name='random_number'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    #path('product/<int:product_id>/', views.client_detail, name='product_detail')
    # Аналогично для продуктов и заказов

]
