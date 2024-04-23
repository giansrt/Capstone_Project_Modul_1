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
def display_vehicles(keyword):
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
        price = 'RP {:,.0f}'.format(price)
        avaliable = "Avaliable" if stock > 0 else "Not Avaliable"
        if not keyword:
            rodas[wheels].append([index, brand,model, wheels, stock, price,avaliable])
        elif keyword == brand.lower() or keyword == model.lower():
            rodas[wheels].append([index, brand,model, wheels, stock, price,avaliable])


    if rodas[4]:
        print('\nFour Wheels :')
        print(tabulate(rodas[4], headers=header_mobil, tablefmt='fancy_grid'))
    if rodas[2]:
        print('\nTwo Wheels:')
        print(tabulate(rodas[2], headers=header_mobil, tablefmt='fancy_grid'))
    if not rodas[4] and not rodas[2]:
        print("No vehicles available !! ")


# ========================Display rental car for user=====================================
def display_rental():
    data_rent.clear()
    header = ['Index','Tenant','Brand','Model','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(data_rental_car):
        if user['username'] == value['tenant'] :
            tenant = value['tenant']
            number_of_car = value['amount']
            price = value['price']
            price = 'RP {:,.0f}'.format(price)
            long_rent = value['long rent']
            start_date = value['start']
            end_date = value['end']
            status = value['status']
            brand = value['brand']
            model = value['model']
            
            data_rent.append([index,tenant,brand,model,number_of_car,start_date,end_date,long_rent,price,'Paid of' if status else 'Debt' ])
    print('\n Your Order ')
    print(tabulate(data_rent, headers=header,tablefmt='fancy_grid'))

# ========================Display rental car for admin=====================================
def display_rental_for_admin():
    data_rent.clear()
    header = ['Index','Tenant','Brand','Model','Amount','Start Rent','End Rent','Long Rent','Rent price','Status Payment']
    for index,value in enumerate(data_rental_car):
        brand = value['brand']
        model = value['model']
        number_of_car = value['amount']
        price = value['price']
        price = 'Rp {:,.0f}'.format(price)
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
                if wheel in ['4','2'] :
                    wheel = int(wheel)
                    break
                else:
                    print('Please insert the right amount of wheel.')
                    
            while True:
                price = input('Input the vehicle price : ')
                if not price.isdigit():
                    print('Please enter numeric value for stock.')
                else:
                    price = int(price)
                    break
        new_vehicle = {
            'brand': brand.capitalize().strip(),  
            'model': model.capitalize().strip(), 
            'stock': stock,
            'wheels': wheel,
            'price': price
        }
        # print(vehicles)
        vehicles.append(new_vehicle)
        # print(vehicles)
        break

# ========================Delete Data=====================================
def delete():
    display_vehicles(None)
    while True:
        option = input('Input vehicle index : ')
        if not option:
            continue
        elif not option.isdigit():
            print('insert the index as number')
            continue
        else:
            option= int(option)
        if option not in range(len(vehicles)):
            print('Input the correct answer ')
            continue
        else:
            print('delete success')
            del vehicles[option]
            break
# =================== Update stock and price ================================
def update_stock_or_price():
    display_vehicles(None)
    while True:
        option = input('Input vehicle index : ')
        if not option:
            continue
        elif not option.isdigit():
            print('Insert a numbers')
            continue
        else:
            option = int(option)
        if option not in range(len(vehicles)):
            print('Input the correct answer ')
        else:
            while True:
                new_stock = input('insert the new stock (just enter to skip): ')
                if not new_stock:
                    break
                if not new_stock.isdigit():
                    print('Insert the right stock')
                    continue
                else:
                    new_stock = int(new_stock)
                    vehicles[option]['stock'] = new_stock
                    break
            while True:
                new_price = input('insert the new price (just enter to skip) : ')
                if not new_price:
                    break
                if not new_price.isdigit():
                    print('Insert the right price')
                    continue
                else:
                    new_price = int(new_price)
                    vehicles[option]['price'] = new_price
                    break  
            break  

# ========================Delete Data rent=====================================
def delete_rental_for_admin():
    display_rental_for_admin()
    while True:
        option = input('Input rent user index : ')
        if not option:
            print('Invalid input ')
            continue
        elif not option.isdigit() :
            print('Invalid input ')
            continue
        else:
            option = int(option)
            if option not in range(len(data_rental_car)):
                print('Invalid Input')
                continue
            else:
                # print(data_rental_car)
                # print(data_rental_car[option]['amont'])
                for key,value in enumerate(vehicles):
                    if value['brand'] == data_rental_car[option]['brand'] and value['model'] == data_rental_car[option]['model']:
                        value['stock'] += data_rental_car[option]['amount'] 
                del data_rental_car[option]
                print('successfully delete rental data')
                break


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
    current_year = dt.datetime.now().year
    
    # Validasi bulan dan tahun
    if not (1 <= month <= 12):
        print("Input the right month !!")
        return False
    
    if not (1 <= day <= 31):
        print("Input the right day  !!")
        return False
    if year < current_year:
        print('Insert valid year !!')
        return False
    
    
    return True

# ======================= Rent Function ==================
def rental_vehicle():
    temp_data = {}
    # display_vehicles(None)
    while True:
        display_vehicles(None)
        option = input('Input the index vehicle : ')
        if not option:
            continue
        if not option.isdigit():
            print('Insert numbers as index')
            continue
        else:
            option = int(option)
        if option not in range(len(vehicles)):
            print('Input the correct answer !! ')
            continue
        elif vehicles[option]['stock'] == 0:
            print(f'Vehicle you choose not avaliable anymore because stock left is {vehicles[option]['stock']}')
            continue
        
        while True:
            amount_car = input('Input the amount of the vehicle you want to rent : ')
            if not amount_car:
                print('insert the amount')
                continue
            elif not amount_car.isdigit():
                print('Insert number to decide amount vehicle')
                continue
            else:
                amount_car = int(amount_car)
            if amount_car > vehicles[option]['stock']:
                print(f'Not enough stock, remaining {vehicles[option]['brand']} model {vehicles[option]['model']} stock is {vehicles[option]['stock']}')
                continue
            if amount_car == 0:
                print(f'Invalid input, remaining stock of {vehicles[option]['brand']} model {vehicles[option]['model']} stock is {vehicles[option]['stock']}')
                continue
            else :
                vehicles[option]['stock'] -= amount_car
                break
        while True:
            date_start = input('Enter start date rent (in format dd/mm/yyyy): ')
            date_end = input('Enter end date rent (in format dd/mm/yyyy): ')
            if not date_start or not date_end:
                print('please insert all date')
                continue
            elif is_valid_date_format(date_start) and is_valid_date_format(date_end):
                day, month, year = map(int, date_start.split('/'))
                day_end, month_end, year_end = map(int, date_end.split('/'))
            else:
                print("Please correct the input dates.")
                continue
            start_date = dt.date(year, month, day)
            end_date = dt.date(year_end,month_end,day_end)
            
            current_day = dt.date.today()
            
            
            if start_date >end_date :
                print('Your input date not valid')
            elif start_date == end_date:
                print('minimum rent is 1 day')
            elif start_date < current_day or end_date < current_day:
                print('Insert the right date')
            else:
                long_rent = (end_date - start_date).days
                break
    
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
    price = 0
    for key, value in enumerate(data_rental_car):
        if value['status'] == False:
            price += value['price']
    print(f'your total price is Rp {price:,}')
    while True :
        user_money = input('Input your money : ')
        if not user_money:
            print('Insert valid value')
            continue
        elif not user_money.isdigit():
            print('Insert valid value')
            continue
        else:
            user_money = int(user_money)
    
        if price > user_money :
            print(f'Your money is not enough, you need to pay {price:,}')
        elif user_money>price:
            print('Thank you')
            print(f'Your change is Rp {user_money - price:,}')
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

# ================== Searching Function ===========================================
def searching():       
    while True:
        print('1. Search')
        print('2.  Exit')
        action = input('You want search/exit (1/2) : ')
        if not action:
            print('Choose what you want to do')
            continue
        elif action.isalpha():
            print('Invalid input')
            continue
        else :
            action = int(action)
        # while True:
        if action == 1:
            keyword = input('Insert name brand or model you want to search : ').lower()
            if not keyword.isalpha():
                print('insert string')
                continue
            if keyword == 'exit':
                break
            else:
                display_vehicles(keyword)
        elif action == 2:
            break
        else:
            print('Invalid input ')
            continue
                
            
        

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
        if any(username.strip().lower() == user['username'] for user in users):
            print(f"There is an account with the username {username}. Please choose a different username.")
        else :
            break
    password = input('Input your password : ')
    temp = {'username' : username, 'password':password, 'role':'user'}
    users.append(temp)
    print('Registration success')
    return temp
# ========================================================================        
        
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
def main():
    welcome_ascii()
    while True :
        print('''
                Welcome
            Need A vehicle
        This Is The Right Place''')
        print('1. Log In')
        print('2. Registration')
        print('3. Exit')
        while True:
            option = input('Insert Your choose: ').strip()
            if option in ['1', '2','3']:
                if option == '1':
                    global user
                    user = login()
                    break
                elif option == '2':
                    user = register()
                    break
                else:
                    print("Wrong input")
                    continue
            else:
                print('Invalid Inpur')
                continue
            
        if user:
            print(f'Login successful as {user["role"]}')
            print()
            if user['role'] == 'admin':
                while True:
                    print('Hi Admin')
                    print('List Menu:\n 1. Display Vehicle\n 2. Add Vehicle\n 3. Remove Vehicle\n 4. Update Stock and/or Price\n 5. Display Rentals\n 6. Delete User Rental Data\n 7. Log out')
                    menu_num = input('Enter your chosen number: ').strip()
                    if menu_num in ['1','2','3','4','5','6','7']:
                        if menu_num == '1':
                            display_vehicles(None)
                        elif menu_num == '2':
                            add_data()
                        elif menu_num == '3':
                            delete()
                        elif menu_num == '4':
                            update_stock_or_price()
                        elif menu_num == '5':
                            if len(data_rental_car) == 0:
                                print('No rentals yet.')
                            else:
                                display_rental_for_admin()
                        elif menu_num == '6':
                            if len(data_rental_car) == 0:
                                print('No rentals yet.')
                            else:
                                delete_rental_for_admin()
                        elif menu_num == '7':
                            break
                    else:
                        print('Invalid Option')
            else: 
                while True:
                    print(f'Welcome {user['username'].capitalize()}')
                    print('List Menu:\n 1. Display Available Vehicles\n 2. Rent Vehicle\n 3. Display Rentals\n 4. Rearch Avaiable Vehiclde with brand/model \n 5. Log out')
                    menu_num = input('Enter your chosen number: ').strip()
                    if menu_num in ['1','2','3','4','5']:
                        if menu_num == '1':
                            display_vehicles(None)
                        elif menu_num == '2':
                            rental_vehicle()
                        elif menu_num == '3':
                            if len(data_rental_car) == 0:
                                print('You haven\'t rented any car yet.')
                            else:
                                display_rental()
                        elif menu_num == '4':
                            searching()
                        elif menu_num == '5':
                            break
                    else:
                        print('Invalid Input .')
        else:
            print('Wrong username or password')







main()