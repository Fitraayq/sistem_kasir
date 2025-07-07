# interface.py

from data_access import get_all_buah
from logic import tambah_ke_keranjang, hitung_total, get_keranjang

def tampilkan_menu():
    print("\n=== Kasir Toko Buah ===")
    print("1. Lihat daftar buah")
    print("2. Beli buah")
    print("3. Lihat keranjang")
    print("4. Selesai & Cetak Struk")
    print("0. Keluar")

def tampilkan_buah():
    print("\nDaftar Buah:")
    for buah in get_all_buah():
        print(f'{buah["id"]}. {buah["nama"]} - Rp{buah["harga"]} (Stok: {buah["stok"]})')

def tampilkan_keranjang():
    keranjang = get_keranjang()
    print("\nKeranjang Belanja:")
    if not keranjang:
        print("Kosong.")
    else:
        for item in keranjang:
            print(f'{item["jumlah"]}x {item["nama"]} - Rp{item["subtotal"]}')
        print(f"Total: Rp{hitung_total()}")

def proses_pembelian():
    tampilkan_buah()
    try:
        buah_id = int(input("Masukkan ID buah yang dibeli: "))
        jumlah = int(input("Jumlah: "))
        if tambah_ke_keranjang(buah_id, jumlah):
            print("Berhasil ditambahkan ke keranjang!")
        else:
            print("Gagal. Stok tidak cukup atau ID salah.")
    except ValueError:
        print("Input tidak valid.")
