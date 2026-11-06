import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("idvgs.csv")
vgs = data[:, 0]
ids = data[:, 1]
vds_value = 1.8
β = 0.0025
vth = 0.56
m = vgs > vth
Vov = vgs[m] - vth

#idvgs linear plot
plt.figure()
plt.plot(vgs[m], ids[m]*1e3, label=f"spice ids | Vds = {vds_value:.1f} V", color = 'blue')
plt.plot(vgs[m], (0.5*β*Vov**2)*1e3, label=f"0.5*β*Vov**2 ids | Vds = {vds_value:.1f} V", color= 'green')
plt.xlabel("Vgs (V)")
plt.ylabel("Id (mA)")
plt.title("ID plot acutal ids vs square law ids | SKY130 NMOS, W/L = 10/1 um, tt")
plt.legend()
plt.grid(True)
plt.savefig("idvgs_squarelaw.png", dpi=150)

##idvgs linear plot
#plt.figure()
#plt.plot(vgs, ids * 1e3, label=f"Vds = {vds_value:.1f} V")
#plt.xlabel("Vgs (V)")
#plt.ylabel("Id (mA)")
#plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
#plt.legend()
#plt.grid(True)
#plt.savefig("idvgs.png", dpi=150)

##idvgs sqrt id plot
#plt.figure()
#plt.plot(vgs,np.sqrt(ids), label=f"Vds = {vds_value:.1f} V")
#plt.xlabel("Vgs (V)")
#plt.ylabel("√Id (√mA)")
#plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
#plt.legend()
#plt.grid(True)
#plt.savefig("sqrt_idvgs.png", dpi=150)
#
##idvgs log plot
#plt.figure()
#plt.semilogy(vgs, ids * 1e3, label=f"Vds = {vds_value:.1f} V")
#plt.xlabel("Vgs (V)")
#plt.ylabel("Id (mA)")
#plt.title("SKY130 NMOS, W/L = 10/1 um, tt")
#plt.legend()
#plt.grid(True)
#plt.savefig("idvgs_log.png", dpi=150)

