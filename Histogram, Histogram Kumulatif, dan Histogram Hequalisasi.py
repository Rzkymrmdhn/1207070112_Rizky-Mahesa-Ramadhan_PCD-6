#Import Library
import numpy as np
import imageio
import matplotlib.pyplot as plt

#Membaca gambar dari direktori
img = imageio.imread("E:/UIN SGD/SMT 6/PENGOLAHAN CITRA DIGITAL/PRAKTIKUM 6/PicsArt_09-12-09.03.11.jpg")

#Mendapatkan resolusi dan type dari gambar
img_height = img.shape[0] #Mendapatkan nilai tinggi gambar
img_width = img.shape[1] #Mendapatkan nilai lebar gambar
img_channel = img.shape[2] #Mendapatkan nilai channel gambar

#MERUBAH GAMBAR MENJADI GRAYSCALE
img_grayscale = np.zeros(img.shape, dtype=np.uint8) #Membuat array numpy baru dengan ukuran yang sama dengan gambar dan tipe data unsigned integer 8-bit

#Looping sepanjang lebar dan tinggi gambar untuk mengakses setiap pixel
for y in range(0, img_height): #Looping semua baris dari gambar
    for x in range(0, img_width): #Looping semua kolom dari gambar

        #Mendapatkan nilai RGB dari pixel saat ini
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        gray = (int(red) + int(green) + int(blue)) / 3 #Menghitung nilai grayscale dari pixel saat ini dengan rumus rata-rata
        img_grayscale[y][x] = (gray, gray, gray) #Menetapkan nilai grayscale yang dihitung ke array numpy baru

#Menampilkan gambar grayscale dengan menggunakan matplotlib        
plt.imshow(img_grayscale)
plt.title("Grayscale") #Menampilkan judul gambar
plt.show() #Menampilkan plot gambar

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#MENAMPILKAN HISTOGRAM GAMBAR GRAYSCALE
#Membuat variabel untuk menyimpan data gambar
hg = np.zeros((256)) #Membuat array kosong dengan ukuran 256 untuk menyimpan nilai histogram

#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):
    hg[x] = 0 #Mengisi setiap elemen array hg dengan nilai 0

#Menghitung nilai dari gambar
for y in range(0, img_height): #Looping semua baris dari gambar
    for x in range(0, img_width): #Looping semua kolom dari gambar
        gray = img_grayscale[y][x][0] #Mengambil nilai keabuan gambar pada koordinat tertentu
        hg[gray] += 1 #Menambahkan nilai pada elemen array hg yang sesuai dengan nilai keabuan tersebut

#Menampilkan Histogram
plt.figure(figsize=(20, 6)) #Membuat figure dengan ukuran 20x6 inch
plt.plot(hg, color="black", linewidth=2.0) #Menampilkan plot histogram dengan warna hitam dan ketebalan garis 2.0
plt.show() #Menampilkan plot histogram

bins = np.linspace(0, 256, 100) #Membuat array bins dengan ukuran 100 yang berisi bilangan dari 0 hingga 256
plt.hist(hg, bins, color="black", alpha=0.5) #Menampilkan histogram dengan menggunakan bins yang sudah dibuat sebelumnya
plt.title("Histogram") #Menampilkan judul histogram
plt.show() #Menampilkan plot histogram

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#MENAMPILKAN HISTOGRAM GAMBAR RGB
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256)) #Membuat array kosong dengan ukuran 256 untuk menyimpan nilai histogram dari komponen warna merah
hgg = np.zeros((256)) #Membuat array kosong dengan ukuran 256 untuk menyimpan nilai histogram dari komponen warna hijau
hgb = np.zeros((256)) #Membuat array kosong dengan ukuran 256 untuk menyimpan nilai histogram dari komponen warna biru
hgrgb = np.zeros((768)) #Membuat array kosong dengan ukuran 768 untuk menyimpan nilai histogram gabungan dari ketiga komponen warna

#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): #Mengisi setiap nilai dalam array hgr, hgg, dan hgb dengan 0 menggunakan loop
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768): #Mengisi setiap nilai dalam array hgrgb dengan 0 menggunakan loop
    hgrgb[x] = 0

#Menghitung nilai dari gambar
for x in range(0, 256): #Mengisi setiap nilai dalam array hgr, hgg, dan hgb dengan 0 menggunakan loop
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768): #Mengisi setiap nilai dalam array hgrgb dengan 0 menggunakan loop
    hgrgb[x] = 0

# th = int(256/64)
temp = [0] #Membuat array kosong temp dengan satu elemen bernilai 0
for y in range(0, img.shape[0]): #Looping untuk setiap baris pada gambar
    for x in range(0, img.shape[1]): #Looping untuk setiap kolom pada gambar
        red = int(img[y][x][0]) #Mengambil nilai komponen warna merah dari pixel pada posisi (y,x)
        green = int(img[y][x][1]) #Mengambil nilai komponen warna hijau dari pixel pada posisi (y,x)
        blue = int(img[y][x][2]) #Mengambil nilai komponen warna biru dari pixel pada posisi (y,x)
        green = green + 256 #Menambahkan nilai 256 pada variabel green, karena akan disimpan di indeks 256 sampai 511 di array hgrgb
        blue = blue + 512 #Menambahkan nilai 512 pada variabel blue, karena akan disimpan di indeks 512 sampai 767 di array hgrgb
#         temp.append(green)
        hgrgb[red] += 1 #Menambahkan nilai pada indeks yang sesuai di array hgrgb untuk komponen warna merah
        hgrgb[green] += 1 #Menambahkan nilai pada indeks yang sesuai di array hgrgb untuk komponen warna hijau
        hgrgb[blue] += 1 #Menambahkan nilai pada indeks yang sesuai di array hgrgb untuk komponen warna biru

binsrgb = np.linspace(0, 768, 100) #Membuat array binsrgb yang berisi 100 nilai yang sama jaraknya dari 0 sampai 768
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5) #Membuat histogram dari data hgrgb dengan menggunakan 100 bins yang telah dibuat dan memberikan warna hitam dengan opacity 0.5
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue") #Menampilkan judul histogram
plt.show() #Menampilkan plot histogram

#Menampilkan Histogram
for y in range(0, img_height): #Looping semua baris dari gambar
    for x in range(0, img_width): #Looping semua kolom dari gambar

        # Menyimpan nilai R, G, B dari setiap pixel
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]

        # Menambahkan 1 pada nilai histogram R, G, B yang sesuai
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

bins = np.linspace(0, 256, 100) #Membuat array bins yang berisi 100 nilai yang sama jaraknya dari 0 sampai 256

#Menampilkan histogram warna merah
plt.hist(hgr, bins, color="red", alpha=0.5) #Membuat histogram dari data hgr dengan menggunakan 100 bins yang telah dibuat dan memberikan warna merah dengan opacity 0.5
plt.title("Histogram Red") #Menampilkan judul histogram merah
plt.show() #Menampilkan plot histogram

plt.hist(hgg, bins, color="green", alpha=0.5) #Membuat histogram dari data hgg dengan menggunakan 100 bins yang telah dibuat dan memberikan warna hijau dengan opacity 0.5
plt.title("Histogram Green") #Menampilkan judul histogram hijau
plt.show() #Menampilkan plot histogram

plt.hist(hgb, bins, color="blue", alpha=0.5) #Membuat histogram dari data hgb dengan menggunakan 100 bins yang telah dibuat dan memberikan warna biru dengan opacity 0.5
plt.title("Histogram Blue") #Menampilkan judul histogram biru
plt.show() #Menampilkan plot histogram

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#MENAMPILKAN HISTOGRAM KUMULATIF
hgk = np.zeros((256)) #Membuat array 1 dimensi dengan 256 elemen dengan nilai awal 0
c = np.zeros((256)) #Membuat array 1 dimensi dengan 256 elemen dengan nilai awal 0

#Inisialisasi nilai awal hgk dan c menjadi 0
for x in range(0, 256): #Looping semua elemen dalam rentang 0 hingga 255
    hgk[x] = 0 #Mengatur nilai elemen dalam array hgk menjadi 0
    c[x] = 0 #Mengatur nilai elemen dalam array c menjadi 0

#Looping untuk setiap pixel gambar
for y in range(0, img_height): #Looping semua baris dari gambar
    for x in range(0, img_width): #Looping semua kolom dari gambar
        gray = img_grayscale[y][x][0] #Mendapatkan nilai grayscale dari piksel pada koordinat (y, x)
        hgk[gray] += 1  #Menambahkan jumlah nilai grayscale pada array hgk sebanyak 1

#Hitung nilai kumulatif untuk setiap nilai grayscale                
c[0] = hgk[0] #Mengatur elemen pertama dari array c menjadi elemen pertama dari array hgk
for x in range(1, 256): #Looping melalui rentang 1 hingga 255
     c[x] = c[x-1] + hgk[x] #Menghitung jumlah kumulatif dari array hgk dan menyimpannya pada array c

hmaxk = c[255] #Hitung nilai maksimal dari arracy c

#Normalisasi nilai c agar berada dalam rentang 0-190
for x in range(0, 256): #Looping melalui semua elemen dalam rentang 0 hingga 255
    c[x] = 190 * c[x] / hmaxk #Normalisasi nilai dari array c dan ubah skala nilainya menjadi 190

#Buat histogram kumulatif dan tampilkan
plt.hist(c, bins, color="black", alpha=0.5) #Membuat histogram dari data arracy c dengan menggunakan bins yang telah dibuat dan memberikan warna hitam dengan opacity 0.5
plt.title("Histogram Grayscale Kumulatif") #Menampilkan judul histogram kumulatif
plt.show() #Menampilkan plot histogram

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#MENAMPILKAN HISTOGRAM HEQUALISASI
hgh = np.zeros((256)) #Membuat array 1 dimensi dengan 256 elemen dengan nilai awal 0
h = np.zeros((256)) #Membuat array 1 dimensi dengan 256 elemen dengan nilai awal 0
c = np.zeros((256)) #Membuat array 1 dimensi dengan 256 elemen dengan nilai awal 0

for x in range(0, 256): #Looping semua elemen dalam rentang 0 hingga 255

    # set nilai hgh, h, dan c pada indeks x menjadi 0
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height): #Looping semua baris dari gambar
    for x in range(0, img_width): #Looping semua kolom dari gambar
        gray = img_grayscale[y][x][0] #Mendapatkan nilai grayscale dari piksel pada koordinat (y, x)
        hgh[gray] += 1 #Menambahkan jumlah nilai grayscale pada array hgh sebanyak 1

                
h[0] = hgh[0] #Set nilai h pada indeks 0 menjadi nilai hgh pada indeks 0
for x in range(1, 256): #Loop untuk setiap nilai x dari 1 hingga 255
     h[x] = h[x-1] + hgh[x]  #Set nilai h pada indeks x menjadi nilai h pada indeks (x-1) ditambah nilai hgh pada indeks x

for x in range(0, 256): #Loop untuk setiap nilai x dari 0 hingga 255
     h[x] = h[x] / img_height / img_width #Set nilai h pada indeks x menjadi nilai h pada indeks x dibagi dengan img_height dan img_width

for x in range(0, 256): #Loop untuk setiap nilai x dari 0 hingga 255
    hgh[x] = 0 #Set nilai hgh pada indeks x menjadi 0
    
for y in range(0, img_height): #Looping semua baris dari gambar
    for x in range(0, img_width): #Looping semua kolom dari gambar
        gray = img_grayscale[y][x][0] #Mendapatkan nilai grayscale dari piksel pada koordinat (y, x)
        gray = h[gray] * 255 #Hitung nilai gray baru dengan mengalikan nilai h pada indeks grayscale dengan 255
        hgh[int(gray)] += 1 #Tambahkan 1 pada nilai hgh pada indeks gray yang sudah dihitung

c[0] = hgh[0] #Set nilai c pada indeks 0 menjadi nilai hgh pada indeks 0
for x in range(1, 256): #Loop untuk setiap nilai x dari 1 hingga 255
     c[x] = c[x-1] + hgh[x] #Set nilai c pada indeks x menjadi nilai c pada indeks (x-1) ditambah nilai hgh pada indeks x

hmaxk = c[255] #Hitung nilai maksimal dari array c

for x in range(0, 256): #Loop untuk setiap nilai x dari 0 hingga 255
    c[x] = 190 * c[x] / hmaxk #Set nilai c pada indeks x menjadi 190 dikali nilai c pada indeks x dibagi oleh hmaxk

plt.hist(c, bins, color="black", alpha=0.5) #Membuat histogram dari data arracy c dengan menggunakan bins yang telah dibuat dan memberikan warna hitam dengan opacity 0.5
plt.title("Histogram Grayscale Hequalisasi") #Menampilkan judul histogram hequalisasi
plt.show() #Menampilkan plot histogram