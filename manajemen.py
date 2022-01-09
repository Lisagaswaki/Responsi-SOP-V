#NIM = 5200411188
#NAMA = Tarsono

total_ram = float(input("Masukan Total Ram  :"))
total_petabit = float(input("Masukan Total Petabit  :"))
jml_perpeta = float(input("Masukan Jumlah Kapasitas Per Petabit  :"))
kapasitas_ram_os = float(input("Masukan Kapasitas RAM Yang digunakan OS  :"))
kapasitas_ram_p1 = float(input("Masukan Kapasitas RAM Yang digunakan Program 1  :"))
kapasitas_ram_p2 = float(input("Masukan Kapasitas RAM Yang digunakan Program 2  :"))

ram_terpakai = (kapasitas_ram_os + kapasitas_ram_p1 + kapasitas_ram_p2)
ram_tdk_terpakai = total_ram - (kapasitas_ram_os + kapasitas_ram_p1 + kapasitas_ram_p2)

blok0 = ram_terpakai
blok1 = ram_tdk_terpakai

print("Total Ram :", total_ram)
print("Total Petabit :", total_petabit)
print("Kapasitas Per Petabit :", jml_perpeta)
print("Ram Terpakai :", ram_terpakai)
print("Ram Tidak Terpakai :", ram_tdk_terpakai)
print("Blok Berjumlah 0 :", blok1)
print("Blok Berjumlah 1 :", blok0)