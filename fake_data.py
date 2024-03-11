from faker import Faker

print(f"ФИО: {Faker('RU').name()}")
print(f"Номер телефона: {Faker('RU').phone_number()}")
print(f"Компания: {Faker('RU').company()}")
print(f"Работа: {Faker('RU').job()}")
print(f"Почта: {Faker('RU').free_email()}")
print(f"Страна проживания: {Faker('RU').country()}")
print(f"Родной адрес: {Faker('RU').address()}")

