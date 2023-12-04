import matplotlib.pyplot as plt # Pour tracer des courbes
import pandas as pd             # Pour lire des fichiers
import numpy as np              # Pour le calcul numérique

data = pd.read_csv("ascenseur.txt")       # lit le fichier du format .txt contenant les données
data.to_csv('ascenseur.csv', index=None)  # convertit .txt au .csv

# extraire les données bruts
tBrut = data["Temps (s)"]       
accXBrut = data["aX (m/s^2)"]
accYBrut = data["aY (m/s^2)"]
accZBrut = data["aZ (m/s^2)"]

# afficher les données bruts
# plt.plot(tBrut, accXBrut, "-b", label="acc X")
# plt.plot(tBrut, accYBrut, "-r", label="acc Y")
# plt.plot(tBrut, accZBrut, "-g", label="acc Z")
# plt.legend(loc="best")
# plt.xlabel(" Temps (s)")
# plt.ylabel(" Accélération (m/s^2)")
# plt.show()

# on extrait les données entre les temps t = 2 et t = 28
# pour ne pas garder que les mesures pendant la montée 

min_index = None # variable pour stocker l'indice du premier tBrut >= 2s
max_index = None # variable pour stocker l'indice du dernier tBrut <= 28s

for i, temps in enumerate(tBrut):                   # trouver min_index et max_index
    if 2 <= temps <= 28:
        if min_index is None or i < min_index:
            min_index = i
        if max_index is None or i > max_index:
            max_index = i


t = np.array(tBrut[min_index:max_index])      
Az = np.array(accZBrut[min_index:max_index])    # extrait les données entre 2 et 28s
Az = Az - Az.mean()                             # Soustrait la valeur moyenne, donc g

N = len(Az)             # taille des tableaux
Vz = np.zeros(N)        # prépare le tableau des vitesses
Z = np.zeros(N)         # prépare le tableau des hauteurs

for i in range (1,N) :              # parcourt tout le tableau
    dt = t[i] - t[i-1]              # calcule le dt
    Vz[i] = Vz[i-1] + Az[i]*dt      # intègre Az pour obtenir vitesse
    Z[i] = Z[i-1] + Vz[i]*dt        # intègre la vitesse pour obtenir distance

fig, axs = plt.subplots(nrows=3, sharex = True)

axs[0].plot(t,Az, "-g", label = "Acc")
axs[0].set_ylabel('Acc (m/s^2)')

axs[1].plot(t,Vz, "-r")
axs[1].set_ylabel('V (m/s)')

axs[2].plot(t,Z, "-b")
axs[2].set_ylabel('Hauteur (m)')

plt.xlabel(" Temps (s)")
plt.show()

