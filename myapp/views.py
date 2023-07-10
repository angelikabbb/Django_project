import datetime
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'myapp:about'},
        {'title': 'Машины парка', 'url_name': 'myapp:cars'},
        {'title': 'Водители парка', 'url_name': 'myapp:drivers'},
        {'title': 'Клиенты', 'url_name': 'myapp:clients'},
        {'title': 'Сотрудники', 'url_name': 'myapp:employee_list'}
        ]
def index(request):
    return HttpResponse('<h1>Main page</h1>')
def index_myapp(request):
    return HttpResponse('<h1>MyApp page</h1>')
def about(request):
    return HttpResponse('<h1>About site</h1>')

def cars(request):
    title = 'Машины'
    cars = Car.objects.all()
    context = {'title': title, 'menu': menu, 'cars': cars}
    return render(request, 'myapp/cars.html', context=context)

# def add_car(request):
#     if request.method == 'GET':
#         title = 'Добавить машину'
#         form = CarForm()
#         context = {'title': title, 'menu': menu, 'form': form}
#         return render(request, 'myapp/car_add.html', context=context)
#
#     if request.method == 'POST':
#         carform = CarForm(request.POST)
#         if carform.is_valid():
#             car = Car()
#             car.brand = carform.cleaned_data['brand']
#             car.model = carform.cleaned_data['model']
#             car.color = carform.cleaned_data['color']
#             car.power = carform.cleaned_data['power']
#             car.year = carform.cleaned_data['year']
#             car.save()
#         return cars(request)

def add_car(request):
    title = 'Добавить машину'

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return cars(request)

    else:
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

def car_card(request, pk):
    car = Car.objects.get(pk=pk)
    title = 'Car Info'
    context = {'menu': menu, 'title': title, 'car': car}

    return render(request, 'myapp/car_card.html', context=context)

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


def driver_card(request, pk):
    title = 'Driver Info'
    driver = Driver.objects.get(pk=pk)
    context = {'menu': menu, 'title': title, 'driver': driver}

    return render(request, 'myapp/driver_card.html', context=context)

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



def client_card(request, pk):
    title = 'Client Info'
    client = Client.objects.get(pk=pk)
    # client = get_object_or_404(Client, pk)
    context = {'menu': menu, 'title': title, 'client': client}

    return render(request, 'myapp/client_card.html', context=context)

class EmployeeList(ListView):
    model = Employee
    template_name = 'myapp/employee_list.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Сотрудники'
        context['count'] = Employee.objects.count()
        context['menu'] = menu

        return context


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'myapp/employee_detail.html'
    context_object_name = 'employee'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'
        context['menu'] = menu
        # context['count'] = Employee.objects.count()
        return context


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'myapp/employee_form.html'


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name_suffix = "myapp/employee_update.html"


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('myapp:employee_list')