# ==========================================
# 1. Mulai Program & Inisialisasi Variabel
# ==========================================
print("==========================================")
print("     APLIKASI KASIR RESTORAN SEDERHANA    ")
print("==========================================")

total_belanja = 0
pesanan_list = []  # Untuk mencatat rincian pesanan di struk

# Daftar Menu Makanan
menu_makanan = {
    1: {"nama": "Nasi Goreng", "harga": 25000},
    2: {"nama": "Mie Ayam", "harga": 15000},
    3: {"nama": "Ayam Geprek", "harga": 20000},
    4: {"nama": "Sate Ayam", "harga": 30000},
    5: {"nama": "Bakso", "harga": 18000},
}

# ==========================================
# 2, 3, & 4. Perulangan Proses Pemesanan
# ==========================================
while True:
    print("\n--- DAFTAR MENU MAKANAN ---")
    for kode, item in menu_makanan.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']:,}")
    print("0. Selesai Memilih")
    print("-" * 27)

    try:
        pilihan = int(input("Pilih Menu (0-5): "))
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
        continue

    # Cek apakah pilihan 0 (Selesai Memilih)
    if pilihan == 0:
        break
    elif pilihan in menu_makanan:
        nama_menu = menu_makanan[pilihan]["nama"]
        harga_menu = menu_makanan[pilihan]["harga"]

        try:
            jumlah = int(input(f"Masukkan jumlah porsi {nama_menu}: "))
            if jumlah <= 0:
                print("Jumlah pesanan harus lebih besar dari 0.")
                continue
        except ValueError:
            print("Input jumlah tidak valid!")
            continue

        # Hitung subtotal dan tambahkan ke total belanja
        subtotal = harga_menu * jumlah
        total_belanja += subtotal

        # Simpan ke daftar pesanan untuk dicetak di struk
        pesanan_list.append(
            {
                "nama": nama_menu,
                "harga": harga_menu,
                "jumlah": jumlah,
                "subtotal": subtotal,
            }
        )

        print(
            f"--> Berhasil menambahkan {jumlah} {nama_menu} (Subtotal: Rp{subtotal:,})"
        )
    else:
        print("Pilihan menu tidak tersedia. Silakan pilih nomor 0-5.")

# ==========================================
# 5. Hitung Diskon
# ==========================================
# Jika total belanja > Rp200.000, dapat diskon 20%, jika tidak diskon 0%
if total_belanja > 200000:
    persen_diskon = 20
    potongan = total_belanja * 0.20
else:
    persen_diskon = 0
    potongan = 0

total_bayar = total_belanja - potongan

# ==========================================
# 6. Tampilkan Struk Pembayaran
# ==========================================
print("\n" + "=" * 40)
print("              STRUK PEMBAYARAN            ")
print("=" * 40)
if len(pesanan_list) == 0:
    print("Tidak ada pesanan yang dilakukan.")
else:
    print(f"{'Menu':<15} | {'Qty':<3} | {'Subtotal'}")
    print("-" * 40)
    for p in pesanan_list:
        print(f"{p['nama']:<15} | {p['jumlah']:<3} | Rp{p['subtotal']:,}")
    print("-" * 40)

print(f"Total Belanja : Rp {total_belanja:,}")
print(f"Diskon ({persen_diskon}%)    : Rp {potongan:,}")
print("-" * 40)
print(f"Total Bayar   : Rp {total_bayar:,}")
print("=" * 40)
print("         Terima Kasih Atas Kunjungan Anda!     ")
print("=" * 40)