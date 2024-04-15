# Contoh data user dan admin (dapat disimpan dalam list of dictionaries)
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "john_doe", "password": "12345", "role": "user"}
]

# Contoh data mobil (dapat disimpan dalam list of dictionaries)
mobil = [
    {"nama": "Toyota Avanza", "stok": 5, "harga_sewa": 200000},
    {"nama": "Honda Civic", "stok": 3, "harga_sewa": 300000},
    {"nama": "Suzuki Ertiga", "stok": 4, "harga_sewa": 250000}
]

# Fungsi untuk login user
def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

# Fungsi untuk menampilkan daftar mobil
def display_mobil():
    print("\nDaftar Mobil Tersedia:")
    for index, mobil in enumerate(mobil):
        print(f"Index: {index}")
        print(f"Nama Mobil: {mobil['nama']}")
        print(f"Stok: {mobil['stok']}")
        print(f"Harga Sewa: Rp {mobil['harga_sewa']}")

# Fungsi untuk menambahkan mobil (hanya bisa dilakukan oleh admin)
def add_mobil(admin_user):
    if admin_user["role"] == "admin":
        nama = input("Masukkan nama mobil baru: ")
        stok = int(input("Masukkan stok mobil baru: "))
        harga_sewa = int(input("Masukkan harga sewa mobil baru: "))
        mobil.append({"nama": nama, "stok": stok, "harga_sewa": harga_sewa})
        print("Mobil baru berhasil ditambahkan.")
    else:
        print("Maaf, hanya admin yang dapat menambahkan mobil.")

# Fungsi untuk melakukan pemesanan mobil (untuk user)
def pesan_mobil(user):
    display_mobil()
    index_mobil = int(input("Masukkan nomor mobil yang ingin dipesan: "))
    if 0 <= index_mobil < len(mobil):
        jumlah = int(input("Masukkan jumlah mobil yang ingin dipesan: "))
        if jumlah > 0 and jumlah <= mobil[index_mobil]["stok"]:
            # Proses pemesanan mobil (contoh implementasi)
            print(f"Pesanan {mobil[index_mobil]['nama']} ({jumlah} unit) berhasil.")
            mobil[index_mobil]["stok"] -= jumlah
        else:
            print("Jumlah mobil tidak valid atau stok tidak mencukupi.")
    else:
        print("Nomor mobil tidak valid.")

# Contoh penggunaan dalam main program
def main():
    while True:
        print("\nSelamat datang di Rental Mobil")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        user = login(username, password)
        
        if user:
            print(f"Login berhasil sebagai {user['role']}")
            if user["role"] == "admin":
                # Menu admin
                print("Menu Admin:")
                print("1. Tambah Mobil")
                print("2. Lihat Daftar Mobil")
                choice = input("Pilih menu: ")
                if choice == "1":
                    add_mobil(user)
                elif choice == "2":
                    display_mobil()
                else:
                    print("Pilihan tidak valid.")
            else:
                # Menu user
                print("Menu User:")
                print("1. Lihat Daftar Mobil")
                print("2. Pesan Mobil")
                choice = input("Pilih menu: ")
                if choice == "1":
                    display_mobil()
                elif choice == "2":
                    pesan_mobil(user)
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Login gagal. Silakan coba lagi.")

if __name__ == "__main__":
    main()
