# Round Robin
# NIM : 5200411188
# Nama : Tarsono

table_prog = []

while True:
    nama_program = input("Masukan Nama Program : ")
    lama_proses = int(input("Masukan Lama Pengerjaan : "))
    jatah_waktu = int(input("Masukan Jatah Waktu : "))

    table_prog.append([lama_proses, jatah_waktu, nama_program])

    y = input("Apakah ingin masukan data lagi [y/n] : ")
    if y.upper() == 'N':
        break

table_prog = sorted(table_prog)

print("Nama Program      Lama Proses      Jatah Waktu")

for i in range(len(table_prog)):
    print(str(table_prog[i][2]) + "\t\t\t" + str(table_prog[i][0]) + "\t\t" + str(table_prog[i][1]))