# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# String

'''
Asuna merupakan seorang novelis, Asuna seringkali menuliskan tulisannya 
di miscrosoft word. Asuna sering sekali menggunakan tool word count
yang ada pada miscrosoft word untuk menghitung jumlah kata yang
ia ketik. Suatu hari Asuna penasaran dan ingin membuat program
yang sama seperti fungsi word count pada miscrosoft word,
tapi karena Asuna hanya seorang novelis biasa yang masih
awam dalam pemograman, Asuna meminta pacarnya senku yang seorang
programer biasa untuk membuatkan program yang diinginkan Asuna
tersebut, Asuna mengilustrasikan program yang ingin dia buat adalah 
sebagai berikut:
1. Program dapat menghitung banyaknya kata yang diketik oleh user, 
2. Program dapat menghitung banyaknya huruf kecil 
dan huruf besar yang diketikan oleh user,
3. Program dapat menghitung jumlah karakter yang telah diketikan
oleh user tanpa spasi dan juga dengan spasi. 
Anggaplah anda adalah pacarnya Asuna, bantulah Asuna untuk 
membuat program seperti kriteria diatas.

'''
'''
Input:
Pada hari ini saya pergi puncak, namun ternyata hari HUJAN.
Proses:
hari HUJAN.
1. hari
2. HUJAN.
2 kata
h >> huruf kecil >> 1
a >> huruf kecil >> 1
H >> huruf besar >> 1
. >> 0

h >> 1
a >> 1
r >> 1
i >> 1
  >> 0

  >> 1
Output:
kata = 10
huruf kecil = 42
huruf besar = 6
karakter tanpa spasi = 50
karakter dengan spasi = 59
'''
# SOURCE CODE

kalimat = input("Masukkan kalimat: ")

# menghitung kata
kata = kalimat.split()
total = len(kata)

# menghitung huruf kecil dan huruf besar
hkecil = 0
hbesar = 0

for i in kalimat:
    if i.islower():
        hkecil += 1
    elif i.isupper():
        hbesar += 1
    else:
        continue

# menghitung total karakter dengan dan tanpa spasi
huruf1 = 0
for i in kalimat:
    if i != " ":
        huruf1 += 1
    else:
        continue

huruf2 = 0
for i in kalimat:
    huruf2 += 1

print("\nKata pada inputan ada:",total,"kata")
print("\nHuruf kecil pada inputan ada:",hkecil,"huruf")
print("\nHuruf besar pada inputan ada:",hbesar,"huruf")
print("\nKarakter tanpa spasi ada:",huruf1,"karakter")
print("\nKarakter dengan spasi ada:",huruf2,"karakter")
