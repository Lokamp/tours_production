import random

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from tours.data import data

tours = data.tours
departures = data.departures


class MainView(View):
    def get(self, request):
        random_tours_main_page = random.sample(list(tours), 6)
        random_tours = {}
        for id_tour, tour_properties in tours.items():
            if id_tour in random_tours_main_page:
                random_tours[id_tour] = tour_properties
        context = {
            'random_tours': random_tours,
        }
        return render(request, "index.html", context)


class DepartureView(View):
    def get(self, request, departure_str_url):
        departures_filter = {}
        for tour_dictionary, tour_properties in tours.items():
            if tour_properties['departure'] == departure_str_url:
                departures_filter[tour_dictionary] = tour_properties
        list_price = [hotel_properties['price'] for dictionary_tours, hotel_properties in departures_filter.items()]
        list_nights = [hotel_properties['nights'] for dictionary_tours, hotel_properties in departures_filter.items()]
        min_price = min(list_price)
        max_price = max(list_price)
        min_nights = min(list_nights)
        max_nights = max(list_nights)
        count_tours = len(departures_filter)
        context = {
            'departures': departures[departure_str_url],
            'departures_filter': departures_filter,
            'min_price': min_price,
            'max_price': max_price,
            'min_nights': min_nights,
            'max_nights': max_nights,
            'count_tours': count_tours,
        }
        return render(request, "departure_str.html", context)


class TourView(View):
    def get(self, request, tour_id_url):
        if not tour_id_url:
            return HttpResponseNotFound(f'Нет автора с id {tour_id_url}. Перейти на <a href="/">Главную страницу</a>')
        context = {
            'tours': tours[tour_id_url],
            'departures': departures,
        }
        return render(request, "tour_id.html", context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404! Попробуйте открыть другую страницу. Главная href="/"')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500! Попробуйте открыть другую страницу. Главная href="/"')
