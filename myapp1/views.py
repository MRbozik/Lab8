from django.shortcuts import render
from .models import Clients, Cars, Repairs
def index_page(request):
    clients = Clients.objects.all()
    cars = Cars.objects.all()
    repairs = Repairs.objects.all()
    context = {
        'clients': clients,
        'cars': cars,
        'repairs': repairs,
        'project_name': 'Лаб 8',
        'student_info': 'Врубевський Олексій Сергійович, КН-20002б',
    }

    return render(request, 'index.html', context)