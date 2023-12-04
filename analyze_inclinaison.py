import matplotlib.pyplot as plt # Pour tracer des courbes
import pandas as pd             # Pour lire des fichiers
import numpy as np              # Pour le calcul numérique

data = pd.read_csv("inclinaison.txt")       # lit le fichier du format .txt contenant les données
data.to_csv('inclinaison.csv', index=None)  # convertit .txt au .csv

tBrut = data["Temps (s)"]

accXBrut = data["aX (m/s^2)"]
accYBrut = data["aY (m/s^2)"]
accZBrut = data["aZ (m/s^2)"]

x = accXBrut.mean()
y = accYBrut.mean()
z = accZBrut.mean()


angleZ = np.arctan(z/np.sqrt(x**2 + y**2))  # calcule de l'incliaison selon Z en rad

# convertit les valeurs d'angles en degrées
angleZdeg = np.degrees(angleZ)

print(f'Inclinasion selon l\'axe oZ {angleZ:.3f} rad, soit {angleZdeg:.3f} degré')

# afficher les données bruts
plt.plot(tBrut, accZBrut, "-g", label="acc Z")
plt.legend(loc="best")
plt.xlabel(" Temps (s)")
plt.ylabel(" Accélération (m/s^2)")
plt.show()
