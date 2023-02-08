from wallet import Customers

customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
customer_2 = Customers('Владимир','Зайцев','Кострома',50)
customer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list=[customer_1, customer_2, customer_3]

for guest in guest_list:
    print(guest.get_guest())