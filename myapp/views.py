import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import CarForm, ClientForm, DriverForm
from .models import Car, Client, Driver

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Машины парка', 'url_name': 'cars'},
        {'title': 'Водители парка', 'url_name': 'drivers'},
        {'title': 'Клиенты', 'url_name': 'clients'},
        ]
def index(request):
    return HttpResponse('<h1>Main page</h1>')
def index_myapp(request):
    return HttpResponse('<h1>MyApp page</h1>')
def about(request):
    return HttpResponse('<h1>About site</h1>')

def cars(request):
    title = 'Машины'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/cars.html', context=context)

def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

    if request.method == 'POST':
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)

def login(request):
    title = 'Войти'
    context = {'title': title, 'menu': menu}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login - {username}, Password - {password}')

    if request.method == 'GET':
        return render(request, 'myapp/login.html', context=context)

def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params - {get_params}')

def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'myapp/clients.html', context=context)
    # print(clients)


def drivers(request):
    title = 'Водители'
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'drivers': drivers}
    return render(request, 'myapp/drivers.html', context=context)


def add_driver(request):
    title = 'Добавить водителя'

    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return drivers(request)

    else:
        form = DriverForm()

        context = {'title': title, 'menu': menu, 'form': form}

        return render(request, 'myapp/driver_add.html', context=context)

def add_client(request):

    title = 'Добавить клиента'

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instance.age = age
            instance.save()
            # form.save()
            return clients(request)

    else:
        form = ClientForm()

        context = {'title': title, 'menu': menu, 'form': form}

        return render(request, 'myapp/client_add.html', context=context)


# def car_detail(request, pk):
#     car = Car.objects.get(pk=pk)
#     title = 'Car detail'
#     context = {"object": car, 'title': title}
#
#     return render(request, 'myapp/car_detail.html', context=context)

def client_card(request, pk):
    title = 'Client Info'
    client = Client.objects.get(pk=pk)
    # client = get_object_or_404(Client, pk)
    context = {'menu': menu, 'title': title, 'client': client}

    return render(request, 'myapp/client_card.html', context=context)