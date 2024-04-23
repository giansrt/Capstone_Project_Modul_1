from tabulate import tabulate 

# Initialize data
admin_data = {"admin": "9999"}
user_data = {"edo": "1234"}
active_renters = {}
rent_history = {}
blocked_users = set()

# Define vehicle data
vehicles = {
    "excavator": [
        {"tipe": "Excavator Mini PC 30", "stock": 10, "harga_unit": 165000, "harga_all_in": 270000},
        {"tipe": "Excavator Mini PC 45", "stock": 10, "harga_unit": 165000, "harga_all_in": 300000},
        {"tipe": "Excavator Mini PC 55", "stock": 5, "harga_unit": 165000, "harga_all_in": 330000},
        {"tipe": "Excavator Mini PC 75", "stock": 5, "harga_unit": 165000, "harga_all_in": 350000},
        {"tipe": "Excavator PC 100", "stock": 15, "harga_unit": 165000, "harga_all_in": 380000},
        {"tipe": "Excavator PC 200", "stock": 15, "harga_unit": 200000, "harga_all_in": 450000},
        {"tipe": "Excavator Long Arm", "stock": 20, "harga_unit": 250000, "harga_all_in": 550000},
        {"tipe": "Excavator Roda Ban", "stock": 20, "harga_unit": 230000, "harga_all_in": 350000}
    ],
    "bulldozer": [
        {"tipe": "Bulldozer D31 Mini", "stock": 5, "harga_unit": 165000, "harga_all_in": 425000},
        {"tipe": "Bulldozer D31 Mini Swamp", "stock": 5, "harga_unit": 175000, "harga_all_in": 435000},
        {"tipe": "Bulldozer D65 Standar", "stock": 10, "harga_unit": 175000, "harga_all_in": 520000},
        {"tipe": "Bulldozer D65 Swamp", "stock": 10, "harga_unit": 165000, "harga_all_in": 650000}
    ]
}

# Function for admin sign in
def admin_sign_in():
    print("\nAdmin Sign In")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == admin_data["admin"]:
        print("Welcome, Admin!")
        admin_menu()
    else:
        print("Invalid username or password.")

# ======================== 1 =========================
#display data
def display_vehicle_data(vehicles):
    # Menyiapkan list untuk mengumpulkan baris tabel
    table_rows = []

    # Iterasi melalui setiap jenis kendaraan (excavator, bulldozer)
    for vehicle_type, vehicle_list in vehicles.items():
        # Iterasi melalui setiap kendaraan dalam jenis tersebut
        for vehicle in vehicle_list:
            # Ekstrak informasi kendaraan
            tipe = vehicle["tipe"]
            stock = vehicle["stock"]
            harga_unit = vehicle["harga_unit"]
            harga_all_in = vehicle["harga_all_in"]

            # Menambahkan data kendaraan ke dalam list untuk tabel
            table_rows.append([vehicle_type, tipe, stock, harga_unit, harga_all_in])

    # Menampilkan tabel menggunakan tabulate
    headers = ["Jenis", "Tipe", "Stock", "Harga/Unit", "Harga All-In"]
    print(tabulate(table_rows, headers=headers, tablefmt="fancy_grid"))

# ========================= 2 =============================
def add_delete_vehicle():
    print("\nAdd/Delete Heavy Vehicle:")
    print("1. Add Vehicle")
    print("2. Delete Vehicle")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nAdd Vehicle:")
        print("1. Harga Sewa Excavator")
        print("2. Harga Sewa Bulldozer")
        vehicle_type_choice = input("Enter your choice (1/2): ")

        if vehicle_type_choice == "1":
            print("\nAdd to Harga Sewa Excavator:")
            tipe_excavator = input("Enter Tipe Excavator: ")
            stock = int(input("Enter Stock: "))
            harga_sewa_unit = int(input("Enter Harga Sewa Unit: "))
            harga_sewa_all_in = int(input("Enter Harga Sewa All In: "))

            vehicles["excavator"].append({
                "tipe": tipe_excavator,
                "stock": stock,
                "harga_unit": harga_sewa_unit,
                "harga_all_in": harga_sewa_all_in
            })
            print("Excavator added successfully.")

        elif vehicle_type_choice == "2":
            print("\nAdd to Harga Sewa Bulldozer:")
            tipe_bulldozer = input("Enter Tipe Bulldozer: ")
            stock = int(input("Enter Stock: "))
            harga_sewa_unit = int(input("Enter Harga Sewa Unit: "))
            harga_sewa_all_in = int(input("Enter Harga Sewa All In: "))

            vehicles["bulldozer"].append({
                "tipe": tipe_bulldozer,
                "stock": stock,
                "harga_unit": harga_sewa_unit,
                "harga_all_in": harga_sewa_all_in
            })
            print("Bulldozer added successfully.")

        else:
            print("Invalid choice.")

    elif choice == "2":
        print("\nDelete Vehicle:")
        print("1. Harga Sewa Excavator")
        print("2. Harga Sewa Bulldozer")
        vehicle_type_choice = input("Enter your choice (1/2): ")

        if vehicle_type_choice == "1":
            print("\nDelete from Harga Sewa Excavator:")
            print("{:<5} {:<20}".format("Index", "Tipe Excavator"))
            for index, excavator in enumerate(vehicles["excavator"], start=1):
                print("{:<5} {:<20}".format(index, excavator["tipe"]))
            index_excavator = int(input("Enter the index of the excavator to delete: "))
            if 1 <= index_excavator <= len(vehicles["excavator"]):
                del vehicles["excavator"][index_excavator - 1]
                print("Excavator deleted successfully.")
            else:
                print("Invalid index.")

        elif vehicle_type_choice == "2":
            print("\nDelete from Harga Sewa Bulldozer:")
            print("{:<5} {:<20}".format("Index", "Tipe Bulldozer"))
            for index, bulldozer in enumerate(vehicles["bulldozer"], start=1):
                print("{:<5} {:<20}".format(index, bulldozer["tipe"]))
            index_bulldozer = int(input("Enter the index of the bulldozer to delete: "))
            if 1 <= index_bulldozer <= len(vehicles["bulldozer"]):
                del vehicles["bulldozer"][index_bulldozer - 1]
                print("Bulldozer deleted successfully.")
            else:
                print("Invalid index.")

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

# # Sample data for vehicles
# vehicles = {
#     "excavator": [
#         {"tipe": "Excavator Mini PC 30", "stock": 10, "harga_unit": 165000, "harga_all_in": 270000},
#         {"tipe": "Excavator Mini PC 45", "stock": 10, "harga_unit": 165000, "harga_all_in": 300000},
#         # Add more excavator data here
#     ],
#     "bulldozer": [
#         {"tipe": "Bulldozer D31 Mini", "stock": 5, "harga_unit": 165000, "harga_all_in": 425000},
#         {"tipe": "Bulldozer D31 Mini Swamp", "stock": 5, "harga_unit": 175000, "harga_all_in": 435000},
#         # Add more bulldozer data here
#     ]
# }

# ====================== 3 ==================== 
# Function to edit sewa alat berat
def edit_sewa_alat_berat():
    print("\nEdit Sewa Alat Berat:")
    print("1. Harga Sewa Excavator")
    print("2. Harga Sewa Bulldozer")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nEdit Harga Sewa Excavator:")
        print("{:<5} {:<20} {:<5} {:<15} {:<15}".format("Index", "Tipe Excavator", "Stock", "Harga Sewa Unit", "Harga Sewa All In"))
        for index, excavator in enumerate(vehicles["excavator"], start=1):
            print("{:<5} {:<20} {:<5} Rp.{:<14}/jam Rp.{:<14}/jam".format(index, excavator["tipe"], excavator["stock"], excavator["harga_unit"], excavator["harga_all_in"]))
        index_excavator = int(input("Enter the index of the excavator you want to edit: "))
        if 1 <= index_excavator <= len(vehicles["excavator"]):
            selected_excavator = vehicles["excavator"][index_excavator - 1]
            print("\nChoose what you want to edit:")
            print("1. Tipe Excavator")
            print("2. Stock")
            print("3. Harga Sewa Unit")
            print("4. Harga Sewa All In")
            edit_choice = input("Enter your choice (1/2/3/4): ")
            if edit_choice == "1":
                new_tipe = input("Enter new Tipe Excavator: ")
                selected_excavator["tipe"] = new_tipe
            elif edit_choice == "2":
                new_stock = int(input("Enter new Stock: "))
                selected_excavator["stock"] = new_stock
            elif edit_choice == "3":
                new_harga_unit = int(input("Enter new Harga Sewa Unit: "))
                selected_excavator["harga_unit"] = new_harga_unit
            elif edit_choice == "4":
                new_harga_all_in = int(input("Enter new Harga Sewa All In: "))
                selected_excavator["harga_all_in"] = new_harga_all_in
            else:
                print("Invalid choice.")
        else:
            print("Invalid index.")

    elif choice == "2":
        print("\nEdit Harga Sewa Bulldozer:")
        print("{:<5} {:<20} {:<5} {:<15} {:<15}".format("Index", "Tipe Bulldozer", "Stock", "Harga Sewa Unit", "Harga Sewa All In"))
        for index, bulldozer in enumerate(vehicles["bulldozer"], start=1):
            print("{:<5} {:<20} {:<5} Rp.{:<14}/jam Rp.{:<14}/jam".format(index, bulldozer["tipe"], bulldozer["stock"], bulldozer["harga_unit"], bulldozer["harga_all_in"]))
        index_bulldozer = int(input("Enter the index of the bulldozer you want to edit: "))
        if 1 <= index_bulldozer <= len(vehicles["bulldozer"]):
            selected_bulldozer = vehicles["bulldozer"][index_bulldozer - 1]
            print("\nChoose what you want to edit:")
            print("1. Tipe Bulldozer")
            print("2. Stock")
            print("3. Harga Sewa Unit")
            print("4. Harga Sewa All In")
            edit_choice = input("Enter your choice (1/2/3/4): ")
            if edit_choice == "1":
                new_tipe = input("Enter new Tipe Bulldozer: ")
                selected_bulldozer["tipe"] = new_tipe
            elif edit_choice == "2":
                new_stock = int(input("Enter new Stock: "))
                selected_bulldozer["stock"] = new_stock
            elif edit_choice == "3":
                new_harga_unit = int(input("Enter new Harga Sewa Unit: "))
                selected_bulldozer["harga_unit"] = new_harga_unit
            elif edit_choice == "4":
                new_harga_all_in = int(input("Enter new Harga Sewa All In: "))
                selected_bulldozer["harga_all_in"] = new_harga_all_in
            else:
                print("Invalid choice.")
        else:
            print("Invalid index.")

    else:
        print("Invalid choice.")

# ======================= 4 ===================
def edit_layanan_jasa():
    print("\nEdit Layanan Jasa:")
    print("1. Jasa Cut and Fill Tanah")
    print("2. Jasa Pemadatan Tanah")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nEdit Jasa Cut and Fill Tanah:")
        print("{:<20} {:<10}".format("Jenis Pekerjaan", "Harga"))
        print("Cut and Fill       Rp 45.000/m^3")
        new_harga = int(input("Enter new Harga per m^3: "))
        print(f"Updated Harga per m^3: Rp {new_harga}/m^3")

    elif choice == "2":
        print("\nEdit Jasa Pemadatan Tanah:")
        print("{:<20} {:<10}".format("Jenis Pekerjaan", "Harga"))
        print("Pemadatan Tanah    Rp 20.000/m^2")
        new_harga = int(input("Enter new Harga per m^2: "))
        print(f"Updated Harga per m^2: Rp {new_harga}/m^2")

    else:
        print("Invalid choice.")

# =============== 5 ==============================
# Function to show active renters
def show_active_renters():
    print("\nActive Renters:")
    for user, rented_items in active_renters.items():
        print(f"{user}: {rented_items}")

# ============ 6 ======================
# Function to show rent history
def show_rent_history():
    print("\nRent History:")
    for user, history in rent_history.items():
        total_price = sum(item["total_price"] for item in history)
        print(f"{user}: Total Price: {total_price}")

# ========= 7 ==========================
# Function to block user
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Display Data")
        print("2. Add/Delete Heavy Vehicle")
        print("3. Edit Sewa Alat Berat")
        print("4. Edit Layanan Jasa")
        print("5. Show Active Renters")
        print("6. Show Rent History")
        print("7. Block User")
        print("8. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_vehicle_data(vehicles)
        elif choice == "2":
            add_delete_vehicle()
        elif choice == "3":
            edit_sewa_alat_berat()
        elif choice == "4":
            edit_layanan_jasa()
        elif choice == "5":
            show_active_renters()
        elif choice == "6":
            show_rent_history()
        elif choice == "7":
            block_user()
        elif choice == "8":
            print("Logged out.")
            return
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\nWelcome to Heavy Vehicle Rent")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sign_in_choice = input("Are you an admin or user? Enter 'admin' or 'user': ")
            if sign_in_choice == "admin":
                admin_sign_in()
            elif sign_in_choice == "user":
                user_sign_in()
            else:
                print("Invalid choice.")
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


main()