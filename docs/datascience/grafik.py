import numpy as np
import matplotlib.pyplot as plt

# Fungsi permintaan dan penawaran
def permintaan(P):
    return -0.1 * P + 400

def penawaran(P):
    return 0.08 * P + 60

# Rentang harga untuk menggambar grafik
harga = np.linspace(1000, 2500, 500)

# Menghitung kuantitas berdasarkan fungsi permintaan dan penawaran
Qd = permintaan(harga)
Qs = penawaran(harga)

# Titik keseimbangan pasar (P = 1888.89, Q = 211.11)
P_eq = 1888.89
Q_eq = permintaan(P_eq)

# Membuat grafik
plt.figure(figsize=(8,6))
plt.plot(harga, Qd, label="Fungsi Permintaan", color='blue')
plt.plot(harga, Qs, label="Fungsi Penawaran", color='green')
plt.axvline(x=P_eq, color='red', linestyle='--', label=f'Titik Keseimbangan: P = {P_eq:.2f}, Q = {Q_eq:.2f}')
plt.axhline(y=Q_eq, color='red', linestyle='--')

# Menambahkan label dan judul
plt.title("Grafik Keseimbangan Pasar", fontsize=14)
plt.xlabel("Harga (P)", fontsize=12)
plt.ylabel("Kuantitas (Q)", fontsize=12)
plt.legend(loc='best')
plt.grid(True)

# Menampilkan grafik
plt.show()
