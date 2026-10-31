import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("idvgs.csv")
vgs = data[:, 0]
ids = data[:, 1]
vds_value = 1.8

plt.figure()
plt.plot(vgs, ids * 1e3, label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("Id (mA)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("idvgs.png", dpi=150)

plt.figure()
plt.semilogy(vgs, ids * 1e3, label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("Id (mA)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("idvgs_log.png", dpi=150)

