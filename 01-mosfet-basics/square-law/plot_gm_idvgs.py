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
Vth = .56 #for vds 1.8V
m = vgs > Vth
vgs_s = vgs[m]
ids_s = ids[m]
gm_s = gm[m]
Vov = vgs_s - Vth

plt.figure()
plt.plot(vgs_s, gm_s, label=f"gradient gm | vds = {vds_value:.1f} V", color='blue')
plt.plot(vgs_s, (2*ids_s)/Vov, label=f"2Id/Vov gm | Vds = {vds_value:.1f} V",color = 'green')
plt.xlabel("Vgs (V)")
plt.ylabel("gm (S)")
plt.title("gradient gm vs. 2Id/Vov gm | SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grad_2IdVov.png", dpi=150)

#Beta = 0.0025
#plt.figure()
#plt.plot(Beta*Vov**2/2, ids * 1e-3, label=f"Vds = {vds_value:.1f} V")
#plt.xlabel("0.5*Beta*Vov^2")
#plt.ylabel("Id (mA)")
#plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
#plt.legend()
#plt.grid(True)
#plt.savefig("2nd.png", dpi=150)

