from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S23 Ultra", "+79123456789")
phone2 = Smartphone("Apple", "iPhone 13 Pro Max", "+79987654321")
phone3 = Smartphone("Realme", "7 Pro", "+79112233445")
phone4 = Smartphone("Sony", "Xperia 5", "+79567891234")
phone5 = Smartphone("Motorolla", "Razr V3", "+79345678912")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model} - {phone.phone_number}")