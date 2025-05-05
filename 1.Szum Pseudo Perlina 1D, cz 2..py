import math
import random
import matplotlib.pyplot as plt
import numpy as np

def permutacje_podw_wygeneruj_v0(DTW, start_maszyny_losowej):
    random.seed(start_maszyny_losowej)
    liczby = list(range(DTW))
    permutacja1 = liczby.copy()
    random.shuffle(permutacja1)
    permutacja2 = liczby.copy()
    return [permutacja1, permutacja2]

print(permutacje_podw_wygeneruj_v0(3,6))

def permutacje_podw_wygeneruj_v1(DTW, start_maszyny_losowej):
    random.seed(start_maszyny_losowej)
    liczby = list(range(DTW))
    random.shuffle(liczby)
    return [liczby, liczby]

print(permutacje_podw_wygeneruj_v0(4,9))

def skoki_perm(tab_perm, wynik_pocz, *skalary):
    wynik = wynik_pocz
    for skl in skalary:
        if skl is not None:
            wynik = tab_perm[wynik + skl]
    return wynik

tab = [2, 0, 4, 1, 3, 2, 0, 4, 1, 3]
print(skoki_perm(tab, 3, 0, 1))
print(skoki_perm(tab, 3, 1, 0))


def funkcja_skrotu_1d_perm_v0(x_c, tab_perm):
    DTW = len(tab_perm)
    skl_0 = x_c % DTW
    wynik = skoki_perm(tab_perm, 0, skl_0)
    return wynik

def funkcja_skrotu_1d_perm_v1(x_c, tab_perm):
    DTW = len(tab_perm) // 2
    skl_0 = x_c % DTW
    skl_1 = math.floor(x_c / DTW) % DTW
    wynik = skoki_perm(tab_perm, 0, skl_0, skl_1)
    return wynik

def funkcja_skrotu_1d_perm_v2(x_c, tab_perm):
    DTW = len(tab_perm) // 2
    skl_0 = x_c % DTW
    skl_1 = math.floor(x_c / DTW) % DTW
    skl_2 = math.floor(x_c / (DTW**2)) % DTW
    wynik = skoki_perm(tab_perm, 0, skl_0, skl_1, skl_2)
    return wynik

def funkcja_skrotu_1d_perm_v3(x_c, tab_perm):
    DTW = len(tab_perm) // 2  # Obliczamy DTW jako połowę długości tablicy permutacji

    #wartości ujemnych
    if x_c < 0:
        czy_ujemne = True
        x_c = -x_c
    else:
        czy_ujemne = False
    wynik = tab_perm[x_c % DTW]
    x_c = math.floor(x_c / DTW)
    while x_c > 0:
        wynik = tab_perm[wynik + (x_c % DTW)]
        x_c = math.floor(x_c / DTW)
    if czy_ujemne:
        wynik = tab_perm[wynik]
    return wynik

# strona 12
tab_wart = [0, 1.0000, 0.0244, 0.6910, 0.3388]
tab_perm = [2, 0, 4, 1, 3, 2, 0, 4, 1, 3]
tab3 = [] #Niech teraz liczby te posłużą jako indeksy w tab_wart. Dzięki temu funkcja szumu dla tych
            #wartości x (x=-1..10) powinna otrzymać następujące wartości wyjściowe :

print("Zastosowanie funkcji skrótu 1d")
for x in range(-1,11):
    tab3.append(funkcja_skrotu_1d_perm_v3(x,tab_perm))

wartosci_tab_wart = [tab_wart[i] for i in tab3]  # Wartości z tab_wart

x_values = list(range(-1, 11))
plt.figure(figsize=(12, 5))
plt.bar(x_values, wartosci_tab_wart)
plt.title('Wartości z tab_wart dla x = -1..10')
plt.xlabel('x')
plt.ylabel('Wartość')
plt.xticks(x_values)
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------------
tab_perm = [1, 2, 0, 1, 2, 0]
tab_x = [0, 0.7, 1]

print("Test dla x od -5 do 5:")
for x in range(-5, 6):
    print(f"x = {x}: {funkcja_skrotu_1d_perm_v3(x, tab_perm)}")


