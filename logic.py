# logic.py

from model import keranjang
from data_access import get_buah_by_id, kurangi_stok
from data_access import get_buah_by_kategori


def tambah_ke_keranjang(buah_id, jumlah):
    buah = get_buah_by_id(buah_id)
    if buah and buah["stok"] >= jumlah:
        if kurangi_stok(buah_id, jumlah):
            keranjang.append({
                "nama": buah["nama"],
                "harga": buah["harga"],
                "jumlah": jumlah,
                "subtotal": buah["harga"] * jumlah
            })
            return True
    return False

def hitung_total():
    return sum(item["subtotal"] for item in keranjang)

def get_keranjang():
    return keranjang

def cari_buah_kategori():
    kategori = input("Masukkan kategori (Lokal/Impor): ")
    hasil = get_buah_by_kategori(kategori)
    if hasil:
        print(f"\nBuah dengan kategori '{kategori}':")
        for buah in hasil:
            print(f'{buah["id"]}. {buah["nama"]} - Rp{buah["harga"]} (Stok: {buah["stok"]})')
    else:
        print("Tidak ada buah dengan kategori tersebut.")

