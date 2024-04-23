from tabulate import tabulate
data_car = []
def display_car(mobil_sorted):
    data_car.clear()
    header_mobil = ['Index', 'Brand','Model', 'Wheels', 'Stock', 'Rent Price per Day','Status']
    rodas = {
        4: [],
        2: []
    }

    # Mengelompokkan mobil berdasarkan jumlah roda
    for index, value in enumerate(mobil_sorted):
        brand = value['brand']
        model = value['model']
        stock = value['stock']
        wheels = value['wheels']
        price = value['price']
        avaliable = "Avaliable" if stock > 0 else "Not Avaliable"
        # if stock > 0:
        #     rodas[wheels].append([index, brand,model, wheels, stock, price,avaliable])
        rodas[wheels].append([index, brand,model, wheels, stock, price,avaliable])

    # Menampilkan tabel dengan label "Roda Empat" dan "Roda Dua"
    if rodas[4]:
        print('\nRoda Empat:')
        print(tabulate(rodas[4], headers=header_mobil, tablefmt='fancy_grid'))
    if rodas[2]:
        print('\nRoda Dua:')
        print(tabulate(rodas[2], headers=header_mobil, tablefmt='fancy_grid'))
    if not rodas[4] and not rodas[2]:
        print("No vehicles available !! ")

# Mendefinisikan daftar kendaraan
vehicles = [
    {"brand": "Toyota", "model": "Camry", "stock": 5,  "wheels": 4, "price" : 3000000},
    {"brand": "Honda", "model": "Civic", "stock": 5, "wheels": 4, "price" : 4000000},
    {"brand": "Ford", "model": "Mustang", "stock": 5,  "wheels": 4, "price" : 5000000},
    {"brand": "Chevrolet", "model": "Malibu", "stock": 5,  "wheels": 4, "price" : 6000000},
    {"brand": "Kia", "model": "Optima", "stock": 5, "wheels": 4, "price" : 7000000},
    {"brand": "Honda", "model": "Super Cub", "stock": 5,  "wheels": 2,"price" : 500000},
    {"brand": "Piaggio", "model": "Vespa", "stock": 5,  "wheels": 2,"price" : 400000},
    {"brand": "Yamaha", "model": "NMAX", "stock": 5, "wheels": 2,"price" : 600000},
    {"brand": "Suzuki", "model": "Address", "stock": 5,  "wheels": 2,"price" : 300000},
    { "brand": "Kawasaki", "model": "Ninja", "stock": 5, "wheels": 2,"price" : 800000}
]

mobil_sorted = sorted(vehicles, key=lambda x : x['wheels'], reverse=True)

# Memanggil fungsi display_car() dengan parameter mobil_sorted
display_car(mobil_sorted)
