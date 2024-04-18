# Capstone Project
from tabulate import tabulate
import datetime as dt
# ============================= Data =====================================
mobil = [
    {"name": "Toyota Avanza", "stock": 5, "price": 200000},
    {"name": "Honda Civic", "stock": 3, "price": 300000},
    {"name": "Suzuki Ertiga", "stock": 4, "price": 250000}
]
users = [
    {'username' : 'admin', 'password':'admin123', 'role':'admin'},
    {'username' : 'gian', 'password':'1', 'role':'user'}
]

# for display main table
data_car = []
   
# contain with car rent by user
data_rental_car = []

# for table
data_rent = []

# ========================Display main table=====================================
def display_car():
    data_car.clear()
    header_mobil = ['Index','Nama Mobil', 'Stock', 'Rent Price per Day']
    for index,value in enumerate(mobil):
        name = value['name']
        stock = value['stock']
        price = value['price']
        if stock > 0 :
            data_car.append([index,name,stock,price])
    if data_car:
        print('\nAviliable Car')
        print(tabulate(data_car, headers=header_mobil,tablefmt='fancy_grid'))
    else:
        print("No car aviliable !! ")
     
# ========================Display rental car for admin=====================================
def display_rental_for_admin():
    data_rent.clear()
    header = ['Index','Tenant','Car Name','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(data_rental_car):
        name = value['name']
        number_of_car = value['amount']
        price = value['price']
        long_rent = value['long rent']
        start_date = value['start']
        end_date = value['end']
        status = value['status']
        tenant = value['tenant']
    
        
        data_rent.append([index,tenant,name,number_of_car,start_date,end_date,long_rent,price,'Paid of' if status else 'Debt' ])
    print('\n Users Order ')
    print(tabulate(data_rent, headers=header,tablefmt='fancy_grid'))

# ========================Add Data=====================================
def add_data():
    new_data = {}
    name = input('Input the vehicle name : ')   
    stock = int(input('Input the vehicle stock : '))   
    price = int(input('Input the vehicle price : '))   
    new_data = {'name': name, 'stock': stock, 'price': price}
    mobil.append(new_data)

# ========================Delete Data=====================================
def delete():
    option = int(input('Input vehicle index : '))
    if option not in range(len(mobil)):
        print('Input the correct answer : ')
    else:
        del mobil[option]
        print(mobil)

# ========================Delete Data rent=====================================
def delete_rental_for_admin():
    display_rental_for_admin()
    option = int(input('Input rent user index : '))
    if option not in range(len(mobil)):
        print('Input the correct answer : ')
    else:
        for key,value in enumerate(mobil):
            if data_rental_car[option]['name'] == value['name']:
                value['stock'] += data_rental_car[option]['amount'] 
        del data_rental_car[option]
    # display_rental_for_admin()

# ========================Display rental car=====================================
def display_rental():
    data_rent.clear()
    header = ['Index','Tenant','Car Name','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(data_rental_car):
        if user['username'] == value['tenant'] :
            tenant = value['tenant']
            name = value['name']
            number_of_car = value['amount']
            price = value['price']
            long_rent = value['long rent']
            start_date = value['start']
            end_date = value['end']
            status = value['status']
            
            data_rent.append([index,tenant,name,number_of_car,start_date,end_date,long_rent,price,'Paid of' if status else 'Debt' ])
    print('\n Your Order ')
    print(tabulate(data_rent, headers=header,tablefmt='fancy_grid'))

# ===================== Validate Format date function ====
def is_valid_date_format(date_string):
    parts = date_string.split('/')
    if len(parts) != 3:
        print("Input the right format !!")
        return False
    
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print("Dont input as a string !!")
        return False
    
    day = int(day)
    month = int(month)
    year = int(year)
    
    # Validasi bulan dan tahun
    if not (1 <= month <= 12):
        print("Input the right month !!")
        return False
    
    if not (1 <= day <= 31):
        print("Input the right day  !!")
        return False
    
    return True

# ======================= Rent Function ==================
def rental_vehicle():
    temp_data = {}
    while True:
        display_car()
        option = int(input('Input the index vehicle : '))
        if option not in range(len(mobil)):
            print('Input the correct answer !! ')
            continue
        while True:
            amount_car = int(input('Input the amount of the car you want to rent : '))
            if amount_car > mobil[option]['stock']:
                print(f'Not enough stock, remaining {mobil[option]['name']} stock is {mobil[option]['stock']}')
                continue
            else :
                break
        date_start = input('Enter start date rent (in format dd/mm/yyyy): ')
        date_end = input('Enter end date rent (in format dd/mm/yyyy): ')
        
        if is_valid_date_format(date_start) and is_valid_date_format(date_end):
            day, month, year = map(int, date_start.split('/'))
            day_end, month_end, year_end = map(int, date_end.split('/'))
        else:
            print("Please correct the input dates.")
            continue
        
        mobil[option]['stock'] -= amount_car
        
        start_date = dt.date(year, month, day)
        end_date = dt.date(year_end,month_end,day_end)
        long_rent = (end_date - start_date).days
    
        for key, value in enumerate(mobil):
            if option == key :
                price_rent =value["price"] * long_rent * amount_car
                temp_data = {'tenant' : user['username'],
                             'name' : value['name'],
                             'amount' : amount_car,
                             'long rent': long_rent,
                             'start' : start_date.strftime('%d %B %Y'),
                             'end':end_date.strftime('%d %B %Y'),
                             'price' : price_rent,
                             'status' : False}

        data_rental_car.append(temp_data)
        data_rent.clear()
        display_rental()
        decision = input('Do you want to make another transaction (yes/no)? ')
        if decision.lower() != 'yes':
            count_peyment()
            break
def count_peyment():
# Count total bill
    price = 0
    for key, value in enumerate(data_rental_car):
        if value['status'] == False:
            price += value['price']
    print(f'your total price is {price}')
    while True :
        user_money = int(input('Input your money : '))
        if price > user_money :
            print(f'Your money is not enough, you need to pay {price}')
        elif user_money>price:
            print('Thank you')
            print(f'Your change is {user_money - price}')
            for ky,value in enumerate(data_rental_car):
                value['status'] = True
            data_rent.clear()
            display_rental()
            break
        elif user_money == price:
            print('Thank you')
            for ky,value in enumerate(data_rental_car):
                value['status'] = True
            data_rent.clear()
            display_rental()
            break

# =============Registration and Log in=========================================
def login():
    username = input('Input username : ')
    password = input('Input password : ')
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

def register():
    print('Let do registration')
    while True:
        username = input('Input one word of your name as username : ')
        if any(username.lower() == user['username'] for user in users):
            print(f"There is an account with the username {username}. Please choose a different username.")
        else :
            break
    password = input('Input your password : ')
    temp = {'username' : username, 'password':password, 'role':'user'}
    users.append(temp)
    return temp
# ========================================================================        
        
        
def main():
    while True:
        welcome_ascii()
        print('''
                Welcome
            Need A vehicle
        This Is The Right Place''')
        option = input('Are you logged in as a user (yes/no) : ')
        if option.lower() == 'yes':
            option = input('Have an account (yes/no) ? ')
            if option.lower() == 'yes':
                global user
                user = login()
            elif option.lower() == 'no':
                user = register() 
            else:
                print("wrong input")
        elif option.lower() == 'no':
            print('Hello admin')
            user  = login()
        else :
            print('Input valid answer !!! ')
            continue

        if user:
            print(f'Log in succes as {user["role"]}')
            if user['role'] == 'admin' :
                while True:
                    print('Hai Admin')
                    print()
                    print('List Menu:\n 1. Display Car\n 2. Adding Car\n 3. Removing Car\n 4. Display Rental\n 5. Delete user rental data\n 6. Exit Program') 
                    menu_num = input('Enter your chosen number: ')
                    if menu_num.isdigit():
                        menu_num = int(menu_num)
                    else:
                        print('Pleas Input Integer not string or include string')
                        continue
                        

                    if menu_num == 1:
                        display_car()
                    elif menu_num == 2:
                        add_data()
                    elif menu_num == 3:
                        delete()
                    elif menu_num == 4:
                        if len(data_rental_car)== 0:
                            print('User don\'t rental yet !!')
                            continue
                        display_rental_for_admin()
                    elif menu_num == 5:
                        if len(data_rental_car)== 0:
                            print('User don\'t rental yet !!')
                            continue
                        delete_rental_for_admin()
                    elif menu_num == 6:
                        break
                    else:
                        print('Invalid option. Please choose again.')
            else:
                while True:
                    print('Welcome User')
                    print()
                    print('List Menu:\n 1. Display Eviliable Car\n 2. Rental Car\n 3. Display Rent \n 4. Exit Program')
                    menu_num = input('Enter your chosen number: ')
                    if menu_num.isdigit():
                        menu_num = int(menu_num)
                    else:
                        print('Pleas Input Integer not string or include string')
                        continue
                    if menu_num == 1:
                        display_car()
                    elif menu_num == 2:
                        rental_vehicle()
                    elif menu_num == 3:
                        if len(data_rental_car)== 0:
                            print('You haven\'t done a rental yet !!')
                            continue
                        display_rental()
                    elif menu_num == 4:
                        break
                    else:
                        print('Invalid option. Please choose again.')
        else:
            print('wrong username / password')
# =============== welcome ascii ==========
def welcome_ascii():
    print()
    spaceship = [
"            \\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___              ",
"             \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\             ",
"              \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |            ",
" ____          \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  _        _ ",
"|  _ \\ ___  _   _  __ _| |  / ___|__ _ _ __ ___  |  _ \\ ___ _ __ | |_ __ _| |",
"| |_) / _ \\| | | |/ _` | | | |   / _` | '__/ __| | |_) / _ \\ '_ \\| __/ _` | |",
"|  _ < (_) | |_| | (_| | | | |__| (_| | |  \\__ \\ |  _ <  __/ | | | || (_| | |",
"|_| \\_\\___/ \\__, |\\__,_|_|  \\____\\__,_|_|  |___/ |_| \\_\\___|_| |_|\\__\\__,_|_|",
"            |___/                                                             "
    ]

    for line in spaceship:
        print(line)
    car = [
"  ___",
"    _-_-  _/\\______\\__",
" _-_-__  / ,-. -|-  ,-.`-.",
"-_- _-_- `( o )----( o )-'",
"           `-'      `-'"
    ]

    for line in car:
        print(line)

main()



    