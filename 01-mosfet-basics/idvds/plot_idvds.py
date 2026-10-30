import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("idvds.csv")
vds = data[:, 0].reshape(-1, 181)
ids = data[:, 1].reshape(-1, 181)
vgs_values = np.arange(0.6, 1.81, 0.2)

for vds_curve, id_curve, vgs in zip(vds, ids, vgs_values):
    plt.plot(vds_curve, id_curve * 1e3, label=f"Vgs = {vgs:.1f} V")

plt.xlabel("Vds (V)")
plt.ylabel("Id (mA)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("idvds.png", dpi=150)
