import numpy as np
import matplotlib.pyplot as plt

def wartosci_losowe_wygeneruj(DTW, start_maszyny_losowej):
    np.random.seed(start_maszyny_losowej)
    tab = np.random.rand(DTW)
    return tab

def wartosci_losowe_wygeneruj_v1(DTW, start_maszyny_losowej):
    np.random.seed(start_maszyny_losowej)
    tab = np.random.rand(DTW)
    tab[0] = 0.0
    tab[1] = 1.0
    return tab

print("Zadanie 1")
print("v0:", wartosci_losowe_wygeneruj(5, 42))
print("v1:", wartosci_losowe_wygeneruj_v1(5, 42))

#-----------------------------------------------------------------------------------------------------------------------------

def funkcja_skrotu_ld_v0(x, DTL):
    return x % DTL

print("\nZadanie 2")
for x in range(-10, 16):
    print(f"x={x:3d} -> {funkcja_skrotu_ld_v0(x, 8)}")

#----------------------------------------------------------------------------------------------------------------------------
print("\nZadanie 3")

def interpolacja_1d_rdzen_vlin(w_l, w_p, delta_x):
    return w_p * delta_x + w_l * (1 - delta_x)

# Test 2: Dla wartości w_l=0.9 i w_p=0.2 jak w instrukcji
print("\nTest 2: Dla w_1=0.9 i w_p=0.2")
w_1, w_p = 0.9, 0.2
for delta in np.linspace(0, 1, 11):
    print(f"delta_x={delta:.1f} -> {interpolacja_1d_rdzen_vlin(w_1, w_p, delta):.4f}")

#-----------------------------------------------------------------------------------------------------------------------------
print("\nZadanie 5")
def funkcja_skrotu_1d(x, DTW):
    return x % DTW

"""---------------------------------------------------------------"""
def interpolacja_1d_rdzen_vlin(w_1, w_p, delta_x):
    return w_p * delta_x + w_1 * (1 - delta_x)


def interpolacja_1d_cala_vlin(x, tab_wart):
    DTW = len(tab_wart)
    if isinstance(x, int) or x.is_integer():
        return tab_wart[funkcja_skrotu_1d(int(x), DTW)]

    x_l = int(np.floor(x))
    x_p = x_l + 1
    delta_x = x - x_l

    i_x_l = funkcja_skrotu_1d(x_l, DTW)
    i_x_p = funkcja_skrotu_1d(x_p, DTW)

    w_l = tab_wart[i_x_l]
    w_p = tab_wart[i_x_p]

    return interpolacja_1d_rdzen_vlin(w_l, w_p, delta_x)

"""---------------------------------------------------------------"""

def przeksztalcenie_wielomianowe(delta_x):
    return (6 * delta_x ** 5) - (15 * delta_x ** 4) + (10 * delta_x ** 3)


def interpolacja_1d_rdzen_vnlin(w_1, w_p, delta_x):
    delta_x = przeksztalcenie_wielomianowe(delta_x)
    return w_p * delta_x + w_1 * (1 - delta_x)


def interpolacja_1d_cala_vnlin(x, tab_wart):
    DTW = len(tab_wart)

    if isinstance(x, int) or x.is_integer():
        return tab_wart[funkcja_skrotu_1d(int(x), DTW)]

    x_l = int(np.floor(x))
    x_p = x_l + 1
    delta_x = x - x_l

    i_x_l = funkcja_skrotu_1d(x_l, DTW)
    i_x_p = funkcja_skrotu_1d(x_p, DTW)

    w_l = tab_wart[i_x_l]
    w_p = tab_wart[i_x_p]

    return interpolacja_1d_rdzen_vnlin(w_l, w_p, delta_x)




DTW = 4
ziarno = 123
tab_wart = wartosci_losowe_wygeneruj_v1(DTW, ziarno)
print("Tablica wartości:", tab_wart)

x_values = np.arange(-4, 8.1, 0.1)
y_lin = [interpolacja_1d_cala_vlin(x, tab_wart) for x in x_values]
y_nlin = [interpolacja_1d_cala_vnlin(x, tab_wart) for x in x_values]


plt.plot(x_values, y_lin, 'b-', label='Interpolacja liniowa')
plt.plot(x_values, y_nlin, 'r-', label='Interpolacja nieliniowa')
plt.plot(range(DTW), tab_wart, 'ko', label='Punkty kontrolne')
plt.xlabel('x')
plt.ylabel('Wartość')
plt.legend()
plt.legend()
plt.grid(True)
plt.show()



