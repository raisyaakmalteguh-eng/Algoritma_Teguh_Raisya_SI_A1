# Program Kelulusan Ujian Matematika Mahasiswa

nama = input("Nama : ")

# Menentukan target nilai berdasarkan nama mahasiswa
if nama.lower() == "andi":
  target = 70
elif nama.lower() == "budi":
  target = 75
elif nama.lower() == "citra":
  target = 80
else:
  target = 70  # nilai default jika nama lain

print(f"Target nilai untuk {nama} adalah {target}")

percobaan = 0
berhasil = False

# Perulangan while maksimal 3 kali percobaan
while percobaan < 3:
  percobaan += 1
  nilai = int(input(f"Nilai {percobaan} : "))

  # Pengecekan apakah nilai sudah mencapai target
  if nilai >= target:
    berhasil = True
    break

print()  # Baris kosong untuk mempercantik tampilan output

# Menampilkan hasil akhir
if berhasil:
  print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
  print(f"{nama} tidak lulus setelah 3 kali percobaan!")