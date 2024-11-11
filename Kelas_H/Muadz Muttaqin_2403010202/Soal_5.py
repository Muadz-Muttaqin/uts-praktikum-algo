# Buatlah program yang meminta pengguna memasukkan sebuah kata dan dua bilangan bulat, yaitu indeks awal dan indeks akhir. Program harus mengeluarkan substring dari kata tersebut berdasarkan indeks awal dan akhir yang



k = input("Masukkan kata: ") #input:Program ini dibuat untuk membuat variable dan inputan kata dari user
i_awal = int(input("Masukkan indeks awal: ")) #input:Program ini dibuat untuk membuat variable dan inputan indeks awal dari user
i_akhir = int(input("Masukkan indeks akhir: "))#input:Program ini dibuat untuk membuat variable dan inputan indeks akhir dari user

proses = k[i_awal:i_akhir]  #proses ini mengecek inputan kata dari user untuk di cek huruf sesuai indeks inputan user

print(f"Substringnya adalah: {proses}")#qutput: menampilkan hasil dari variabel proses