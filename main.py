# main.py

from interface import tampilkan_menu, tampilkan_buah, tampilkan_keranjang, proses_pembelian
from logic import cari_buah_kategori

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_buah()
        elif pilihan == "2":
            proses_pembelian()
        elif pilihan == "3":
            tampilkan_keranjang()
        elif pilihan == "4":
            tampilkan_keranjang()
            print("\nTerima kasih telah berbelanja!")
            break
        elif pilihan == "5":
            cari_buah_kategori()

        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
