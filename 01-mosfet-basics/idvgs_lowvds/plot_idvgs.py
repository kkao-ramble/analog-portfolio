import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("idvgs_lowvds.csv")
vgs = data[:, 0]
ids = data[:, 1]
vds_value = 0.1

#idvgs linear plot
plt.figure()
plt.plot(vgs, ids * 1e3, label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("Id (mA)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("idvgs_lowvds.png", dpi=150)

#idvgs sqrt id plot
plt.figure()
plt.plot(vgs,np.sqrt(ids), label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("√Id (√mA)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("sqrt_idvgs_lowvds.png", dpi=150)

#idvgs log plot
plt.figure()
plt.semilogy(vgs, ids * 1e3, label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("Id (mA)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("idvgs_log_lowvds.png", dpi=150)

