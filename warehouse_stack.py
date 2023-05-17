#tumpukan barang di sebuah gudang(stack)
stack = []

def tambah_barang(stack, barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru} berhasil ditambahkan ke dalam stack.")
    
def hapus_barang_terakhir(stack):
    if len(stack)== 0:
        print("stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir} berhasil dihapus dari stack.")
        
def tampilkan_barang_teratas(stack):
    if len(stack) == 0:
        print("stack ksosng, tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print(f"barang teratas didalam stack adalah{barang_teratas}.")
        
while True:
    print("\nGudang saat ini:" ,stack)
    print("Menu:")
    print("1. tambah barang")
    print("2. hapus barang")
    print("3. tampilkan barang")
    print("4. keluar")
    
    pilihan = input("masukkan pilihan anda (1/2/3/4):")
        
        
