from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger('django')


# def index(request):
#     return HttpResponse(f'shamil')

def index(request):
    logger.info('Главная страница была посещена.')
    return render(request, 'my_dz_1/index.html', {'title': 'Главная страница'})


def about(request):
    inf = '''
    Меня зовут Шамиль Мамедов
    мне 45 я из солнечного города Баку,
    мне очень повезло что есть возможность учиться на этой платформе
    и знакомиться с новыми людьми


    '''
    logger.info('"О себе" страница была посещена.')
    return render(request, 'my_dz_1/about.html', {'inf': inf, 'title': 'О себе'})