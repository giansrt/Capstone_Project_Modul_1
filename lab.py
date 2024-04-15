# Capstone Project
from tabulate import tabulate
import datetime as dt
# =================DATA=====================================
mobil = [
    {"name": "Toyota Avanza", "stock": 5, "price": 200000},
    {"name": "Honda Civic", "stock": 3, "price": 300000},
    {"name": "Suzuki Ertiga", "stock": 4, "price": 250000}
]
# for display main table
data_car = []
header_mobil = ['Index','Nama Mobil', 'Stock', 'Rent Price per Day']
for index,value in enumerate(mobil):
    name = value['name']
    stock = value['stock']
    price = value['price']
    if stock > 0 :
        data_car.append([index,name,stock,price])

# contain with car rent by user
rental_car = []
data_rent = []



# ========================Display rental car=====================================
def display_rental():
    header = ['Index','Car Name','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(rental_car):
        name = value['name']
        number_of_car = value['amount']
        price = value['price']
        long_rent = value['long rent']
        start_date = value['start']
        end_date = value['end']
        status = value['status']
        
        data_rent.append([index,name,number_of_car,start_date,end_date,long_rent,price,'Padi of' if status else 'Debt' ])
        print('\n Your Order ')
        print(tabulate(data_rent, headers=header,tablefmt='fancy_grid'))   
            


# ========================Display main table=====================================
def display_car():
    if data_car:
        print('\nAviliable Car')
        print(tabulate(data_car, headers=header_mobil,tablefmt='fancy_grid'))
    else:
        print("No car aviliable !! ")



# ========================Add Data=====================================
def add_data():
    new_data = {}
    name = input('Input the viachel name : ')   
    stock = int(input('Input the viachel stock : '))   
    price = int(input('Input the viachel price : '))   
    new_data = {'name': name, 'stock': stock, 'price': price}
    mobil.append(new_data)

# ========================Delete=====================================
def delete():
    option = int(input('Input vehicle index : '))
    if option not in range(len(mobil)):
        print('Input the correct answer : ')
    else:
        del mobil[option]
        print(mobil)

# ========================Rental=====================================
def rental_viechle():
    temp_data = {}
    while True:
        display_car()
        option = int(input('Input the index vehicle : '))
        if option not in range(len(mobil)):
            print('Input the correct answer : ')
            continue
        amount_car = int(input('Input the amount of the car : '))
        
        date_start = input('Enter start date rent(in format dd/mm/yyyy): ')
        date_end = input('Enter end date rent (in format dd/mm/yyyy): ')
        day, month, year = map(int, date_start.split('/'))
        day_end, month_end, year_end = map(int, date_end.split('/'))
        
        start_date = dt.date(year, month, day)
        end_date = dt.date(year_end,month_end,day_end)
        
        long_rent = (end_date - start_date).days
    
        for key, value in enumerate(mobil):
            if option == key :
                price_rent =value["price"] * long_rent * amount_car
                temp_data = {'name' : value['name'],
                             'amount' : amount_car,
                             'long rent': long_rent,
                             'start' : start_date.strftime('%d %B %Y'),
                             'end':end_date.strftime('%d %B %Y'),
                             'price' : price_rent,
                             'status' : False}

        rental_car.append(temp_data)
        data_rent.clear()
        display_rental()
        decision = input('Do you want to make another transaction (yes/no)? ')
        if decision.lower() != 'yes':
            count_peyment()
            break
def count_peyment():
# Count total bill
    price = 0
    for key, value in enumerate(rental_car):
        price += value['price']
    print(f'your total price is {price}')
    while True :
        user_money = int(input('Input your money : '))
        if price > user_money :
            print(f'Your money is not enough, you need to pay {price}')
        elif user_money>price:
            print('Thank you')
            print(f'Your change is {user_money - price}')
            for ky,value in enumerate(rental_car):
                value['status'] = True
            data_rent.clear()
            display_rental()
            break
        elif user_money == price:
            print('Thank you')
            for ky,value in enumerate(rental_car):
                value['status'] = True
            data_rent.clear()
            display_rental()
            break
    
def update_data():
    while True:
        option = int(input('Input index of the car you want to update: '))
        if option < 0 or option >= len(mobil):
            print('Invalid index. Please input the correct index.')
            continue
        car = mobil[option]
        new_name = input('Input the new name (press enter to skip): ')
        new_stock = input('Input the new stock (press enter to skip): ')
        new_price = input('Input the new price (press enter to skip): ')
        
        if new_name:
            car['name'] = new_name
        if new_stock:
            car['stock'] = int(new_stock)
        if new_price:
            car['price'] = int(new_price)
        
        decision = input('Do you want to update another data (yes/no)? ')
        if decision.lower() != 'yes':
            break

# ===============main for now ========================
def main():
    while True:
        print('\nWelcome to Fruits Market')
        print('''List Menu: 
        1. Display Eviliable Car
        2. Adding Car
        3. Removing Car 
        4. Rental Car 
        5. Exit Program ''')

        menu_num = input('Enter your chosen number: ')
        menu_num = int(menu_num)

        if menu_num == 1:
            display_car()
        elif menu_num == 2:
            add_data()
        elif menu_num == 3:
            delete()
        elif menu_num == 4:
            rental_viechle()
        elif menu_num == 5:
            break
        else:
            print('Invalid option. Please choose again.')

main()