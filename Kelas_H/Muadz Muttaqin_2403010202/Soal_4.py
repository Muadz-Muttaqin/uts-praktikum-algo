# Buatlah program yang meminta pengguna untuk memasukkan sebuah kalimat, lalu menghitung dan menampilkan jumlah huruf vokal (a, e, i, o, u) di dalam kalimat tersebut.


kalimat = input("Masukkan kalimat: ")#input:Program ini dibuat untuk membuat variable dan inputan kalimat dari user

vokal = 'aeiouAEIOU'#program ini untuk mengisi nilai pada variabel vokal  dengan huruf vokal
j_vokal = sum(1 for char in kalimat if char in vokal)#program ini bertujuan untuk menghitung karakter dari inputan user dan mengecek jumlah huruf vokal

print(f"Jumlah huruf vokal: {j_vokal}")#qutput: menampilkan hasil dari variabel j_vokal



