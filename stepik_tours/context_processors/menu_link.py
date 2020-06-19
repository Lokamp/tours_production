def menu(request):
    dict_link = {'link': {1: {"city": "/departure/msk/", "name": "Из Москвы"},
                 2: {"city": "/departure/spb/", "name": "Из Петербурга"},
                 3: {"city": "/departure/nsk/", "name": "Из Новосибирска"},
                 4: {"city": "/departure/ekb/", "name": "Из Екатеринбурга"},
                 5: {"city": "/departure/kazan/", "name": "Из Казани"}}}
    return dict_link
