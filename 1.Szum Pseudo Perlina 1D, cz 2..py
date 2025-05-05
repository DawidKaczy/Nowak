import math

def skokl_perm(tab_perm, wynik_pocz, *skalary):
    wynik = wynik_pocz
    for skl in skalary:
        if skl is not None:
            wynik = tab_perm[wynik + skl]
    return wynik

tab = [2, 0, 4, 1, 3, 2, 0, 4, 1, 3]
print(skokl_perm(tab, 3, 0, 1))
print(skokl_perm(tab, 3, 1, 0))


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


tab_perm = [1, 2, 0, 1, 2, 0]
tab_x = [0, 0.7, 1]

print("Test dla x od -5 do 5:")
for x in range(-5, 6):
    print(f"x = {x}: {funkcja_skrotu_1d_perm_v3(x, tab_perm)}")


