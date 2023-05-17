class Queue:
    def __init__(self):
        self.transaksi = []

    def enqueue(self, transaksi):
        self.transaksi.append(transaksi)
        print(f"Transaksi {transaksi} telah ditambahkan ke dalam antrean.")

    def dequeue(self):
        if not self.is_empty():
            transaksi = self.transaksi.pop(0)
            print(f"Transaksi {transaksi} yang dilayani telah dihapus.")
        else:
            print("Antrean kosong. Tidak ada transaksi yang dilayani.")

    def peek(self):
        if not self.is_empty():
            print(f"Transaksi berikutnya: {self.transaksi[0]}")
        else:
            print("Antrean kosong. Tidak ada transaksi yang ditampilkan.")

    def is_empty(self):
        return len(self.transaksi) == 0


queue = Queue()

while True:
    print("\nMenu")
    print("1. Tambahkan transaksi")
    print("2. hapus transaksi yang telah dilayani")
    print("3. Tampilkan transaksi berikutnya")
    print("0. Keluar")
    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        jenis_transaksi = input("Masukkan jenis transaksi: ")
        info_transaksi= f"{nama_pelanggan} ({jenis_transaksi})"
        queue.enqueue(info_transaksi)
    elif choice == "2":
        queue.dequeue()
    elif choice == "3":
        queue.peek()
    elif choice == "0":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
