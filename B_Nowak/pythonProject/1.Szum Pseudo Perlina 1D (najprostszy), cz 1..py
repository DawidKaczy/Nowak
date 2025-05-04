import numpy as np
import matplotlib.pyplot as plt

def wartosci_losowe_wygeneruj(DTW, start_maszyny_losowej):
    np.random.seed(start_maszyny_losowej)
    tab = np.random.rand(DTW)
    return tab

DTW = 8
seed = 42

tab_wart = wartosci_losowe_wygeneruj(DTW, seed)
print("Wygenerowana tablica wartości losowych:")
print(tab_wart)

plt.figure(figsize=(10, 4))
plt.bar(range(DTW), tab_wart)
plt.xlabel('Indeks')
plt.ylabel('Wartość')
plt.ylim(0, 1.1)
plt.xticks(range(DTW))
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()