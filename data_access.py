# data_access.py

from model import buah_list

def get_all_buah():
    return buah_list

def get_buah_by_id(buah_id):
    for buah in buah_list:
        if buah["id"] == buah_id:
            return buah
    return None

def get_buah_by_kategori(kategori):
    return [buah for buah in buah_list if buah["kategori"].lower() == kategori.lower()]

def kurangi_stok(buah_id, jumlah):
    for buah in buah_list:
        if buah["id"] == buah_id and buah["stok"] >= jumlah:
            buah["stok"] -= jumlah
            return True
    return False
