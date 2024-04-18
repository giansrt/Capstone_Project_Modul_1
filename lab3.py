# Capstone Project
from tabulate import tabulate
import datetime as dt
# ============================= Data =====================================
vehicles = [
    {'brand': 'Honda', 'model': 'Civic', 'stock': 5, 'wheels': 4, 'price': 4000000},
    {'brand': 'Honda', 'model': 'Super Cub', 'stock': 5, 'wheels': 2, 'price': 500000},
    {'brand': 'Kawasaki', 'model': 'Ninja', 'stock': 5, 'wheels': 2, 'price': 800000},
    {'brand': 'Toyota', 'model': 'Camry', 'stock': 5, 'wheels': 4, 'price': 3000000},
    {'brand': 'Suzuki', 'model': 'Address', 'stock': 5, 'wheels': 2, 'price': 300000},
    {'brand': 'Ford', 'model': 'Mustang', 'stock': 5, 'wheels': 4, 'price': 5000000},
    {'brand': 'Piaggio', 'model': 'Vespa', 'stock': 5, 'wheels': 2, 'price': 400000},
    {'brand': 'Chevrolet', 'model': 'Malibu', 'stock': 5, 'wheels': 4, 'price': 6000000},
    {'brand': 'Yamaha', 'model': 'NMAX', 'stock': 5, 'wheels': 2, 'price': 600000},
    {'brand': 'Kia', 'model': 'Optima', 'stock': 5, 'wheels': 4, 'price': 7000000}
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
def display_vehicles():
    mobil_sorted = sorted(vehicles, key=lambda x : x['wheels'], reverse=True)
    data_car.clear()
    header_mobil = ['Index', 'Brand','Model', 'Wheels', 'Stock', 'Rent Price per Day','Status']
    rodas = {
        4: [],
        2: []
    }

    for index, value in enumerate(mobil_sorted):
        brand = value['brand']
        model = value['model']
        stock = value['stock']
        wheels = value['wheels']
        price = value['price']
        avaliable = "Avaliable" if stock > 0 else "Not Avaliable"
        rodas[wheels].append([index, brand,model, wheels, stock, price,avaliable])

    if rodas[4]:
        print('\nRoda Empat:')
        print(tabulate(rodas[4], headers=header_mobil, tablefmt='fancy_grid'))
    if rodas[2]:
        print('\nRoda Dua:')
        print(tabulate(rodas[2], headers=header_mobil, tablefmt='fancy_grid'))
    if not rodas[4] and not rodas[2]:
        print("No vehicles available !! ")

# ========================Display main table=====================================
def display_vehicles_for_edit():
    data_car.clear()
    header_mobil = ['Index', 'Brand','Model', 'Wheels', 'Stock', 'Rent Price per Day','Status']
    rodas = {
        4: [],
        2: []
    }

    for index, value in enumerate(vehicles):
        brand = value['brand']
        model = value['model']
        stock = value['stock']
        wheels = value['wheels']
        price = value['price']
        avaliable = "Avaliable" if stock > 0 else "Not Avaliable"
        rodas[wheels].append([index, brand,model, wheels, stock, price,avaliable])

    if rodas[4]:
        print('\nRoda Empat:')
        print(tabulate(rodas[4], headers=header_mobil, tablefmt='fancy_grid'))
    if rodas[2]:
        print('\nRoda Dua:')
        print(tabulate(rodas[2], headers=header_mobil, tablefmt='fancy_grid'))
    if not rodas[4] and not rodas[2]:
        print("No vehicles available !! ")

# ========================Display rental car for admin=====================================
def display_rental_for_admin():
    data_rent.clear()
    header = ['Index','Tenant','Brand','Model','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(data_rental_car):
        brand = value['brand']
        model = value['model']
        number_of_car = value['amount']
        price = value['price']
        long_rent = value['long rent']
        start_date = value['start']
        end_date = value['end']
        status = value['status']
        tenant = value['tenant']
    
        
        data_rent.append([index,tenant,brand,model,number_of_car,start_date,end_date,long_rent,price,'Paid of' if status else 'Debt' ])
    print('\n Users Order ')
    print(tabulate(data_rent, headers=header,tablefmt='fancy_grid'))

# ========================Add Data=====================================
def add_data():
    while True:
        brand = input('Input the vehicle brand : ') 
        model = input('Input the vehicle model : ')
        exists = any(v['brand'].lower() == brand.lower() and v['model'].lower() == model.lower() for v in vehicles)
        if exists:
            print('Vehicle already exists!')
            continue
        else:
            while True:
                stock = input('Input the vehicle stock : ')
                if not stock.isdigit():
                    print('Please enter numeric value for stock.')
                else:
                    stock = int(stock)
                    break
            while True:
                wheel = input('Insert amount the vehicle wheel (4/2) : ')
                if wheel == '4' or wheel == '2' :
                    wheel = int(wheel)
                    break
                else:
                    print('Please insert the right amount of wheel.')
                    
            while True:
                price = input('Input the vehicle price : ')
                if not price.isdigit():
                    print('Please enter numeric value for stock.')
                else:
                    stock = int(price)
                    break
        new_vehicle = {
            'brand': brand.capitalize().strip(),  
            'model': model.capitalize().strip(), 
            'stock': stock,
            'wheels': wheel,
            'price': price
        }
        print(vehicles)
        vehicles.append(new_vehicle)
        print(vehicles)
        break

# ========================Delete Data=====================================
def delete():
    display_vehicles_for_edit()
    option = int(input('Input vehicle index : '))
    if option not in range(len(vehicles)):
        print('Input the correct answer : ')
    else:
        del vehicles[option]

# ========================Delete Data rent=====================================
def delete_rental_for_admin():
    display_rental_for_admin()
    option = int(input('Input rent user index : '))
    if option not in range(len(vehicles)):
        print('Input the correct answer : ')
    else:
        for key,value in enumerate(vehicles):
            if data_rental_car[option]['brand'] == value['brand'] and data_rental_car[option]['model'] == value['model'] :
                value['stock'] += data_rental_car[option]['amount'] 
        del data_rental_car[option]
    # display_rental_for_admin()

# ========================Display rental car=====================================
def display_rental():
    data_rent.clear()
    header = ['Index','Tenant','Brand','Model','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(data_rental_car):
        if user['username'] == value['tenant'] :
            tenant = value['tenant']
            number_of_car = value['amount']
            price = value['price']
            long_rent = value['long rent']
            start_date = value['start']
            end_date = value['end']
            status = value['status']
            brand = value['brand']
            model = value['model']
            
            data_rent.append([index,tenant,brand,model,number_of_car,start_date,end_date,long_rent,price,'Paid of' if status else 'Debt' ])
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
        display_vehicles_for_edit()
        option = int(input('Input the index vehicle : '))
        if option not in range(len(vehicles)):
            print('Input the correct answer !! ')
            continue
        while True:
            amount_car = int(input('Input the amount of the car you want to rent : '))
            if amount_car > vehicles[option]['stock']:
                print(f'Not enough stock, remaining {vehicles[option]['brand']} model {vehicles[option]['model']} stock is {vehicles[option]['stock']}')
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
        
        vehicles[option]['stock'] -= amount_car
        
        start_date = dt.date(year, month, day)
        end_date = dt.date(year_end,month_end,day_end)
        long_rent = (end_date - start_date).days
    
        for key, value in enumerate(vehicles):
            if option == key :
                price_rent =value["price"] * long_rent * amount_car
                temp_data = {'tenant' : user['username'],
                             'brand' : value['brand'],
                             'model' : value['model'],
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
    print()
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
    welcome_ascii()
    print('''
            Welcome
        Need A vehicle
    This Is The Right Place''')
    validation_mesg()
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
# ================ messge ================
def validation_mesg():
    while True:
        option = input('Are you logged in as a user (yes/no): ').strip().lower()
        if option in ['yes', 'no']:
            if option == 'yes':
                account_option = input('Do you have an account (yes/no) ? ').strip().lower()
                if account_option in ['yes', 'no']:
                    if account_option == 'yes':
                        global user
                        user = login()
                    elif account_option == 'no':
                        user = register()
                    else:
                        print("Wrong input")
                        continue
                else:
                    print('You can only input yes/no')
                    continue
            else:  
                print('Hello admin')
                user = login()  
        else:
            print('Please input yes or no.')
            continue

        if user:
            print(f'Login successful as {user["role"]}')
            print()
            if user['role'] == 'admin':
                while True:
                    print('Hi Admin')
                    print('List Menu:\n 1. Display Cars\n 2. Add Car\n 3. Remove Car\n 4. Display Rentals\n 5. Delete User Rental Data\n 6. Exit Program')
                    menu_num = input('Enter your chosen number: ')
                    if menu_num.isdigit():
                        menu_num = int(menu_num)
                        if menu_num == 1:
                            display_vehicles()
                        elif menu_num == 2:
                            add_data()
                        elif menu_num == 3:
                            delete()
                        elif menu_num == 4:
                            if len(data_rental_car) == 0:
                                print('No rentals yet.')
                            else:
                                display_rental_for_admin()
                        elif menu_num == 5:
                            if len(data_rental_car) == 0:
                                print('No rentals yet.')
                            else:
                                delete_rental_for_admin()
                        elif menu_num == 6:
                            break
                        else:
                            print('Invalid option. Please choose again.')
                    else:
                        print('Please input an integer.')
            else:  # Regular user
                while True:
                    print(f'Welcome {user['username'].capitalize()}')
                    print('List Menu:\n 1. Display Available Vehicles\n 2. Rent a Car\n 3. Display Rentals \n 4. Exit Program')
                    menu_num = input('Enter your chosen number: ')
                    if menu_num.isdigit():
                        menu_num = int(menu_num)
                        if menu_num == 1:
                            display_vehicles()
                        elif menu_num == 2:
                            rental_vehicle()
                        elif menu_num == 3:
                            if len(data_rental_car) == 0:
                                print('You haven\'t rented any car yet.')
                            else:
                                display_rental()
                        elif menu_num == 4:
                            break
                        else:
                            print('Invalid option. Please choose again.')
                    else:
                        print('Please input an integer.')
        else:
            print('Wrong username or password')







main()



    