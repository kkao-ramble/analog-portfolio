import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("idvgs.csv")
vgs = data[:, 0]
ids = data[:, 1]
gm = np.gradient(ids,vgs)
vds_value = 1.8
n = 1.56

plt.figure()
plt.plot(vgs, gm, label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("gm (S)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("gm_vgs.png", dpi=150)

plt.figure()
plt.semilogy(vgs, np.abs(gm/ids), label=f"Vds = {vds_value:.1f} V")
plt.xlabel("Vgs (V)")
plt.ylabel("gm/Id (1/V)")
plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
plt.axhline(1/(n*0.026), linestyle = "--", label = "q/(nkT)")
plt.legend()
plt.grid(True)
plt.savefig("gmid_vgs_log.png", dpi=150)

