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

    return interpolacja_1d_rdzen_vlin(w_1, w_p, delta_x)


DTW = 8
seed = 42
tab_wart = wartosci_losowe_wygeneruj_v1(DTW, seed)



x_int = np.arange(-DTW, 2 * DTW)
y_int = [tab_wart[funkcja_skrotu_1d(x, DTW)] for x in x_int]

# Interpolacja
x_fine = np.linspace(-DTW, 2 * DTW, 500)
y_fine = [interpolacja_1d_cala_vlin(x, tab_wart) for x in x_fine]
plt.plot(x_fine, y_fine, 'r-', linewidth=2, label='Interpolacja liniowa')

# Punkty z tablicy
plt.plot(range(DTW), tab_wart, 'bo', markersize=8, label='Oryginalne punkty')

plt.title('Interpolacja liniowa dla szumu Perlina')
plt.xlabel('x')
plt.ylabel('Wartość')
plt.ylim(-0.1, 1.1)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
