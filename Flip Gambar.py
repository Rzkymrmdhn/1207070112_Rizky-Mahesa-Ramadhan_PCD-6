#Import library
import numpy as np
import imageio
import matplotlib.pyplot as plt

#Membaca gambar dari direktori
img = imageio.imread("E:/UIN SGD/SMT 6/PENGOLAHAN CITRA DIGITAL/PRAKTIKUM 6/PicsArt_09-12-09.03.11.jpg")

#Mendapatkan resolusi dan type dari gambar
img_height = img.shape[0] #Mendapatkan nilai tinggi gambar
img_width = img.shape[1] #Mendapatkan nilai lebar gambar
img_channel = img.shape[2] #Mendapatkan nilai channel gambar
img_type = img.dtype #Mendapatkan tipe data gambar

#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type) #Membuat array kosong dengan bentuk yang sama seperti gambar untuk gambar dibalik secara horizontal
img_flip_vertical = np.zeros(img.shape, img_type) #Membuat array kosong dengan bentuk yang sama seperti gambar untuk gambar dibalik secara vertikal

#Membalik gambar secara horizontal
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c] #Gambar dibalik horizontal dengan cara menukar posisi piksel pada sumbu x

#Membalik gambar secara vertical
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c] #Gambar dibalik vertikal dengan cara menukar posisi piksel pada sumbu y

#Menampilkan hasil gambar asli
plt.imshow(img)
plt.title("Gambar Asli")
plt.show()

#Menampilkan hasil gambar dibalik horizontal
plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()

#Menampilkan hasil gambar dibalik vertical
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()