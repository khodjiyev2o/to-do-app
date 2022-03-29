from django.shortcuts import render,redirect

import requests
from .forms import CityForm,CarForm
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView, DetailView
from .models import Weather, Car
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def approval(request):
    cars = Car.objects.all()
    if request.user.is_superuser:
        if request.method == "POST":
            id_list=request.POST.getlist('boxes')
            Car.objects.all().update(approved="False")
            for id in id_list:
                Car.objects.filter(id=id).update(approved="True")
            messages.success(request, ('Successfully updated!'))
            return redirect('market')
    else:
        messages.success(request, ('You are not a superuser!'))
        return redirect('user_profile')


    return render(request,'approval.html',{'cars':cars})
def user_profile(request):
    if request.user.is_authenticated:
        cars = Car.objects.filter(user=request.user.id)
        return render(request,'user_profile.html',{'cars':cars})
    else:
        return redirect('main')




def search(request):
    if request.method == "POST":
        search = request.POST['searched']
        cars = Car.objects.filter(carname__contains=search)

        return render(request, 'search.html', {'search': search, 'cars': cars})


def market(request):
    data = []
    cars = Car.objects.all().order_by('-id')
    nums=[]

    for car in cars:
        venue_owner = User.objects.get(pk=car.user)
        car_info = {
            'id': car.id,
            'owner_phone': car.owner_phone,
            'description': car.description,
            'price': car.price,
            'carname': car.carname,
            'user':  car.user,
            'venue_owner':venue_owner,
            'photo':car.photo,
            'approved':car.approved,
        }

        data.append(car_info)

    paginator = Paginator(data,6)  # Show 6 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums="a"*page_obj.paginator.num_pages
    return render(request, 'market.html', {'cars': page_obj,'nums':nums})




def pricing(request):
    if request.method == "POST":
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            user= form.save(commit=False)
            user.user=request.user.id
            user.save()
            messages.success(request, ('Wait for your item to be approved,it will take some time!'))
            return HttpResponseRedirect('market')
    car = CarForm()

    return render(request, 'pricing.html', {'form': car})





def index(request):
    data = []
    form = []
    key = '219b58b008da2b4c6be2ff72d76be973'
    api = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CityForm(request.POST)
        # check whether it's valid:
        form.save()
        print(request.GET.get)
    form = CityForm()
    cities = Weather.objects.all()
    for city in cities:
        resp_json = requests.get(api.format(city.city)).json()
        city_info = {
            'id': city.id,
            "city": city.city,
            "temp": resp_json['main']['temp'],
            "humidity": resp_json['main']['humidity'],
            "icon": resp_json['weather'][0]['icon'],
            "description": resp_json['weather'][0]['description'],
            "country": resp_json['sys']['country']
        }
        data.append(city_info)
    return render(request, 'main.html', {'data': data, 'form': form})



class CarUpdateView(UpdateView):
    model = Car
    template_name = 'pricing.html'
    form_class=CarForm
    success_url = '/market'



class WeatherDeleteView(DeleteView):
    model = Weather
    success_url = '/main'
    fields = ['city']



class CarDeleteView(DeleteView):
    model = Car
    success_url = '/market'
    fields = ['carname','description','owner','price']

class CarDetailView(DetailView):
    model = Car
    template_name = 'view.html'
    context_object_name = 'cars'
