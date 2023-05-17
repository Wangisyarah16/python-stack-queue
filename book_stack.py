class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Book:
    def __init__(self, nama_buku, pengarang):
        self.nama_buku = nama_buku
        self.pengarang = pengarang


def tambah_buku(stack):
    nama_buku = input("Masukkan nama buku: ")
    pengarang = input("Masukkan pengarang buku: ")
    book = Book(nama_buku, pengarang)
    stack.push(book)
    print("Buku berhasil ditambahkan ke dalam tumpukan.")


def hapus_buku(stack):
    if not stack.is_empty():
        hapus_buku = stack.pop()
        print(f"Buku '{hapus_buku.nama_buku}' oleh {hapus_buku.pengarang} dihapus dari tumpukan.")
    else:
        print("Tumpukan kosong. Tidak ada buku yang dapat dihapus.")


def tampilkan_buku_teratas(stack):
    if not stack.is_empty():
        buku_teratas = stack.peek()
        print("Buku teratas:")
        print(f"Judul: {buku_teratas.nama_buku}")
        print(f"Pengarang: {buku_teratas.pengarang}")
    else:
        print("Tumpukan kosong. Tidak ada buku yang ditampilkan.")


def main():
    stack = Stack()
    while True:
        print("\nPilih operasi:")
        print("1. Tambahkan buku")
        print("2. Hapus buku terakhir")
        print("3. Tampilkan buku teratas")
        print("4. Keluar")
        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == "1":
            tambah_buku(stack)
        elif choice == "2":
            hapus_buku(stack)
        elif choice == "3":
            tampilkan_buku_teratas(stack)
        elif choice == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
