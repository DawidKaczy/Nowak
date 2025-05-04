import numpy as np
import matplotlib.pyplot as plt


def funkcja_skrotu_1d(x, DTW):
    return x % DTW


def wartosci_losowe_wygeneruj_v1(DTW, start_maszyny_losowej):
    np.random.seed(start_maszyny_losowej)
    tab = np.random.rand(DTW)
    tab[0] = 0.0
    tab[1] = 1.0
    return tab

DTW = 8
seed = 11

print("Test funkcji skrótu:")

print(funkcja_skrotu_1d(4,4))

print(funkcja_skrotu_1d(-1,4))



#2.Generowanie tablicy z wartościami losowymi zawierającej 0.0 i 1.0
tab_start = wartosci_losowe_wygeneruj_v1(DTW, seed)
print("\nWygenerowana tablica z 0.0 i 1.0:")
print(tab_start)

# 3. Wizualizacja cykliczności
plt.figure(figsize=(12, 5))
x_values = range(DTW)
y_values = [tab_start[funkcja_skrotu_1d(x, DTW)] for x in x_values]

plt.bar(x_values, y_values)

plt.title('')
plt.xlabel('x (dowolna liczba całkowita)')
plt.ylabel('Wartość')
plt.show()