from tabulate import tabulate
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
data_car = []
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
        


def update():
    display_vehicles_for_edit()
    option = int(input('Input vehicle index : '))
    if option not in range(len(vehicles)):
        print('Input the correct answer : ')
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
update()

