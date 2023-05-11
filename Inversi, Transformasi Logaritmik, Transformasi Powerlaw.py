#Import Library
import numpy as np
import imageio
import matplotlib.pyplot as plt

#Membaca gambar dari direktori
img = imageio.imread("E:/UIN SGD/SMT 6/PENGOLAHAN CITRA DIGITAL/PRAKTIKUM 6/PicsArt_09-12-09.03.11.jpg")
img_height = img.shape[0] #Mendapatkan nilai tinggi gambar
img_width = img.shape[1] #Mendapatkan nilai lebar gambar
img_channel = img.shape[2] #Mendapatkan nilai channel gambar

#INVERSI
#Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8) #Membuat array numpy baru dengan ukuran yang sama dengan gambar dan tipe data unsigned integer 8-bit

#Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0] #Mendapatkan nilai red pada koordinat (x,y)
            green = img[y][x][1] #Mendapatkan nilai green pada koordinat (x,y)
            blue = img[y][x][2] #Mendapatkan nilai blue pada koordinat (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3 #Menghitung nilai rata-rata dari red, green, dan blue untuk mendapatkan nilai grayscale
            gray = nilai - gray #Melakukan inversi pada nilai grayscale
            img_inversi[y][x] = (gray, gray, gray) #Menyimpan nilai grayscale yang sudah diinversi pada variabel img_inversi

#Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0] #Mendapatkan nilai red pada koordinat (x,y)
            red = nilai - red  #Melakukan inversi pada nilai red
            green = img[y][x][1] #Mendapatkan nilai green pada koordinat (x,y)
            green = nilai - green #Mendapatkan nilai green pada koordinat (x,y)
            blue = img[y][x][2] #Mendapatkan nilai blue pada koordinat (x,y)
            blue = nilai - blue #Melakukan inversi pada nilai blue
            img_inversi[y][x] = (red, green, blue) #Menyimpan nilai rgb yang sudah di-inversi pada variabel img_inversi

#Menampilkan hasil inversi grayscale
inversi_grayscale(255) #Menggunakan fungsi inversi grayscale dengan parameter nilai maksimal 255
plt.imshow(img_inversi) #Menampilkan gambar hasil inversi grayscale
plt.title("Inversi Grayscale") #Menampilkan judul pada gambar hasil inversi grayscale
plt.show() #Menampilkan plot gambar

#Menampilkan hasil inversi RGB
inversi_rgb(255) #Menampilkan judul pada gambar hasil inversi grayscale
plt.imshow(img_inversi)
plt.title("Inversi RGB") #Menampilkan judul pada gambar hasil inversi RGB
plt.show() #Menampilkan plot gambar

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#LOG
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8) #Membuat array numpy baru dengan ukuran yang sama dengan gambar dan tipe data unsigned integer 8-bit

#Mendefinisikan fungsi untuk log
def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0] #Mendapatkan nilai red pada koordinat (x,y)
            green = img[y][x][1] #Mendapatkan nilai green pada koordinat (x,y)
            blue = img[y][x][2] #Mendapatkan nilai blue pada koordinat (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3 #Menghitung nilai rata-rata dari red, green, dan blue untuk mendapatkan nilai grayscale
            gray = int(c * np.log(gray + 1)) #Melakukan operasi log pada nilai piksel, kemudian dikali dengan konstanta c dan dibulatkan ke integer terdekat
            
            #Jika nilai piksel lebih besar dari 255, maka atur nilai piksel menjadi 255
            if gray > 255: 
                gray = 255
            
            #Jika nilai piksel lebih kecil dari 0, maka atur nilai piksel menjadi 0
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray)

#Menampilkan hasil log
log(30) #Menggunakan fungsi log dengan konstanta c=30
plt.imshow(img_log)
plt.title("Log") #Menampilkan judul pada gambar
plt.show() #Menampilkan plot gambar

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#INVERSI DAN LOG
#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8) #Membuat array numpy baru dengan ukuran yang sama dengan gambar dan tipe data unsigned integer 8-bit

#Mendefinisikan fungsi untuk inversi log
def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0] #Mendapatkan nilai red pada koordinat (x,y)
            green = img[y][x][1] #Mendapatkan nilai green pada koordinat (x,y)
            blue = img[y][x][2] #Mendapatkan nilai blue pada koordinat (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3 #Menghitung nilai rata-rata dari red, green, dan blue untuk mendapatkan nilai grayscale
            gray = int(c * np.log(255 - gray + 1)) #Menghitung nilai inversi log dengan parameter c
            
            #Jika nilai piksel lebih besar dari 255, maka atur nilai piksel menjadi 255
            if gray > 255:
                gray = 255
            
            #Jika nilai piksel lebih kecil dari 0, maka atur nilai piksel menjadi 0
            if gray < 0:
                gray = 0
            img_inlog[y][x] = (gray, gray, gray) #Atur nilai piksel pada gambar hasil inversi

#Menampilkan hasil inversi log
inlog(30) #Menggunakan fungsi inlog dengan konstanta c=30
plt.imshow(img_inlog)
plt.title("Inversi & Log") #Menampilkan judul pada gambar
plt.show() #Menampilkan plot gambar

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#NTH POWER
#Membuat variabel img_nthpower untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8) #Membuat array numpy baru dengan ukuran yang sama dengan gambar dan tipe data unsigned integer 8-bit

#Mendefinisikan fungsi untuk nth power
def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0] #Mendapatkan nilai red pada koordinat (x,y)
            green = img[y][x][1] #Mendapatkan nilai green pada koordinat (x,y)
            blue = img[y][x][2] #Mendapatkan nilai blue pada koordinat (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3 #Menghitung nilai rata-rata dari red, green, dan blue untuk mendapatkan nilai grayscale
            gray = int(thc * pow(gray, thy))

            #Jika nilai piksel lebih besar dari 255, maka atur nilai piksel menjadi 255
            if gray > 255:
                gray = 255
            
            #Jika nilai piksel lebih kecil dari 0, maka atur nilai piksel menjadi 0
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

#Menampilkan hasil
nthpower(50, 100) #Menggunakan fungsi nthpower dengan konstanta c = 50 dan y = 100
plt.imshow(img_nthpower)
plt.title("Nth Power") #Menampilkan judul pada gambar
plt.show() #Menampilkan plot gambar

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#NTH ROOT POWER
#Membuat variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)

#Membuat fungsi untuk nth root power
def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0] #Mendapatkan nilai red pada koordinat (x,y)
            green = img[y][x][1] #Mendapatkan nilai green pada koordinat (x,y)
            blue = img[y][x][2] #Mendapatkan nilai blue pada koordinat (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3 #Menghitung nilai rata-rata dari red, green, dan blue untuk mendapatkan nilai grayscale
            gray = int(thc * pow(gray, 1./thy))

            #Jika nilai piksel lebih besar dari 255, maka atur nilai piksel menjadi 255
            if gray > 255:
                gray = 255

            #Jika nilai piksel lebih kecil dari 0, maka atur nilai piksel menjadi 0
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

#Menampilkan hasil
nthrootpower(50, 100) #Menggunakan fungsi nthrootpower dengan konstanta c = 50 dan y = 100
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power") #Menampilkan judul pada gambar
plt.show() #Menampilkan plot gambar
