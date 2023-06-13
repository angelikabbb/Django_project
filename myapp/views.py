from django.shortcuts import render
from django.http import HttpResponse
from .forms import CarForm

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
    pass

def drivers(request):
    pass

