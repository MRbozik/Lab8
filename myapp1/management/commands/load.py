from django.core.management.base import BaseCommand
from myapp1.models import Clients, Cars, Repairs  # Замініть "your_app" на правильну назву вашого додатку
import random

class Command(BaseCommand):
    help = 'Populate Clients, Cars, and Repairs tables with data'

    def handle(self, *args, **options):
        # Додаємо клієнтів (6 клієнтів)
        clients_data = [
            {
                'CompanyName': 'Клієнт1',
                'BankAccount': '1234567890',
                'Phone': '123-456-7890',
                'ContactPerson': 'Контактна особа1',
                'Address': 'Адреса1',
            },
            {
                'CompanyName': 'Клієнт2',
                'BankAccount': '2345678901',
                'Phone': '234-567-8901',
                'ContactPerson': 'Контактна особа2',
                'Address': 'Адреса2',
            },
            {
                'CompanyName': 'Клієнт3',
                'BankAccount': '3456789012',
                'Phone': '345-678-9012',
                'ContactPerson': 'Контактна особа3',
                'Address': 'Адреса3',
            },
            {
                'CompanyName': 'Клієнт4',
                'BankAccount': '4567890123',
                'Phone': '456-789-0123',
                'ContactPerson': 'Контактна особа4',
                'Address': 'Адреса4',
            },
            {
                'CompanyName': 'Клієнт5',
                'BankAccount': '5678901234',
                'Phone': '567-890-1234',
                'ContactPerson': 'Контактна особа5',
                'Address': 'Адреса5',
            },
            {
                'CompanyName': 'Клієнт6',
                'BankAccount': '6789012345',
                'Phone': '678-901-2345',
                'ContactPerson': 'Контактна особа6',
                'Address': 'Адреса6',
            },
        ]

        for data in clients_data:
            client = Clients(**data)
            client.save()

        # Додаємо автомобілі (4 марки автомобілів)
        car_brands = ['fiesta', 'focus', 'fusion', 'mondeo']

        for _ in range(6):  # Додамо по 1 автомобілю кожної марки для 6 клієнтів
            data = {
                'CarBrand': random.choice(car_brands),
                'NewCarPrice': random.uniform(10000, 25000),
                'ClientCode': Clients.objects.order_by('?').first()
            }
            car = Cars(**data)
            car.save()

        # Додаємо ремонти (15 ремонтів)
        repair_types = ['гарантійний', 'плановий', 'капітальний']

        for _ in range(15):
            data = {
                'RepairStartDate': '2023-11-05',
                'CarCode': Cars.objects.order_by('?').first(),
                'RepairType': random.choice(repair_types),
                'HourlyRepairCost': random.uniform(30, 70),
                'Discount': random.randint(0, 10),
                'HoursRequired': random.randint(1, 5),
            }
            repair = Repairs(**data)
            repair.save()

        self.stdout.write(self.style.SUCCESS('Successfully filled Clients, Cars, and Repairs tables'))
