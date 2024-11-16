# List untuk menyimpan data mahasiswa
DM = []

while True:
    print("\nMasukkan data mahasiswa")
    nama = input("Nama: ")
    nim = input("Masukkan Nim: ")
    tugas = float(input("Nilai Tugas (0-100): "))
    uts = float(input("Nilai UTS (0-100): "))
    uas = float(input("Nilai UAS (0-100): "))

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    # tambahkan data ke dalam list
    DM.append({
        "Nama": nama,
        "Nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })

    # menambah data lagi
    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data == 't':
        break

# Tampilkan daftar data mahasiswa
print("\nDaftar Data Mahasiswa:")
print("No | Nama       | Nim      | Tugas | UTS   | UAS   | Nilai Akhir")
print("-" * 70)
for i, mahasiswa in enumerate(DM, start=1):
    print(f"{i:2} | {mahasiswa['Nama']:<10} |  {mahasiswa['Nim']:<7} | {mahasiswa['tugas']:<5} | {mahasiswa['uts']:<5} | {mahasiswa['uas']:<5} | {mahasiswa['nilai_akhir']:.2f}")
