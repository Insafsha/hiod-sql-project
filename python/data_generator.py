"""
Генерация реалистичных данных для БД туристической компании.

Скрипт создаёт SQL-файлы:
- fill_clients_realistic.sql
- fill_tours_realistic.sql
- fill_orders_realistic.sql
- fill_discounts_realistic.sql

Все данные синтетические, сгенерированы с помощью Faker.
"""
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('ru_RU')

# === Генерация клиентов ===
clients_lines = []
for _ in range(150):
    full_name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    is_regular = random.choice(['TRUE', 'FALSE'])
    is_blacklisted = 'TRUE' if is_regular == 'FALSE' and random.random() < 0.1 else 'FALSE'
    clients_lines.append(f"('{full_name}', '{email}', '{phone}', {is_regular}, {is_blacklisted})")

clients_sql = "INSERT INTO clients (full_name, email, phone, is_regular, is_blacklisted) VALUES\n"
clients_sql += ",\n".join(clients_lines) + ";"

with open("fill_clients_realistic.sql", "w", encoding="utf-8") as f:
    f.write(clients_sql)

# === Генерация заказов ===
orders_lines = []
num_orders = 300
max_client_id = 150
max_tour_id = 100
statuses = ['оплачен', 'в процессе', 'отменён']

for _ in range(num_orders):
    client_id = random.randint(1, max_client_id)
    tour_id = random.randint(1, max_tour_id)
    order_date = datetime.today() - timedelta(days=random.randint(0, 180))
    order_date_str = order_date.strftime('%Y-%m-%d')
    status = random.choices(statuses, weights=[0.6, 0.3, 0.1])[0]
    total_cost = random.randint(50000, 150000)
    orders_lines.append(f"({client_id}, {tour_id}, '{order_date_str}', '{status}', {total_cost})")

orders_sql = "INSERT INTO orders (client_id, tour_id, order_date, status, total_cost) VALUES\n"
orders_sql += ",\n".join(orders_lines) + ";"

with open("fill_orders_realistic.sql", "w", encoding="utf-8") as f:
    f.write(orders_sql)

# === Генерация скидок ===
discount_lines = []
num_discounts = 30
max_client_id = 150
used_client_ids = set()
reasons = ['Постоянный клиент', 'Жалоба на отель', 'Промокод', 'Сезонная акция', 'День рождения']
percentages = [5, 10, 15, 20]

while len(discount_lines) < num_discounts:
    client_id = random.randint(1, max_client_id)
    if client_id in used_client_ids:
        continue
    used_client_ids.add(client_id)
    percentage = random.choice(percentages)
    reason = random.choice(reasons)
    discount_lines.append(f"({client_id}, {percentage}, '{reason}')")

discounts_sql = "INSERT INTO discounts (client_id, percentage, reason) VALUES\n"
discounts_sql += ",\n".join(discount_lines) + ";"

with open("fill_discounts_realistic.sql", "w", encoding="utf-8") as f:
    f.write(discounts_sql)

# === Генерация туров ===
tours_lines = []
countries = ['Турция', 'Франция', 'Греция', 'Италия', 'ОАЭ', 'Испания', 'Норвегия', 'Таиланд', 'Кипр', 'Чехия']
regions = {
    'Турция': ['Анталья', 'Бодрум', 'Аланья'],
    'Франция': ['Париж', 'Ницца', 'Лион'],
    'Греция': ['Афины', 'Салоники', 'Ираклион'],
    'Италия': ['Рим', 'Милан', 'Венеция'],
    'ОАЭ': ['Дубай', 'Абу-Даби'],
    'Испания': ['Барселона', 'Мадрид'],
    'Норвегия': ['Берген', 'Осло'],
    'Таиланд': ['Пхукет', 'Бангкок'],
    'Кипр': ['Ларнака', 'Никосия'],
    'Чехия': ['Прага', 'Брно']
}
types = ['пляжный', 'экскурсионный', 'горнолыжный', 'круиз', 'шоп-тур']

for _ in range(100):
    country = random.choice(countries)
    region = random.choice(regions[country])
    hotel = fake.company() + ' Hotel'
    tour_type = random.choice(types)
    duration = random.randint(3, 14)
    price = random.randint(50000, 150000)
    tours_lines.append(f"('{country}', '{region}', '{hotel}', '{tour_type}', {duration}, {price})")

tours_sql = "INSERT INTO tours (country, region, hotel_name, tour_type, duration_days, price) VALUES\n"
tours_sql += ",\n".join(tours_lines) + ";"

with open("fill_tours_realistic.sql", "w", encoding="utf-8") as f:
    f.write(tours_sql)
