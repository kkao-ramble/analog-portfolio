import numpy as np

data = np.loadtxt("idvgs.csv")
vgs = data[:, 0]
ids = np.abs(data[:, 1])
gm = np.gradient(ids, vgs)

# 1. Subthreshold swing: fit a line to log10(Id) vs Vgs
m = (vgs > 0.15) & (vgs < 0.4)
slope, intercept = np.polyfit(vgs[m], np.log10(ids[m]), 1)  # decades per volt
swing = 1000 / slope                                        # mV per decade
n = swing / 59.5                                            # 59.5 mV/dec is ideal at 300 K
print(f"swing = {swing:.1f} mV/dec, n = {n:.2f}")

# 2. Peak gm/Id and where it occurs
ratio = gm / ids
i = np.argmax(ratio)
print(f"peak gm/Id = {ratio[i]:.1f} 1/V at Vgs = {vgs[i]:.2f} V")

# 3. gm inflection: where gm is rising fastest
dgm = np.gradient(gm, vgs)
j = np.argmax(dgm)
print(f"gm inflection at Vgs = {vgs[j]:.2f} V")

# Vth extraction
limits = [0.05, 0.1, 0.15]
s = np.gradient(np.sqrt(ids), vgs)
k = np.argmax(s)
for limit in limits:
    m = (vgs > vgs[k] - limit) & (vgs < vgs[k] + limit)
    slope, intercept = np.polyfit(vgs[m], np.sqrt(ids[m]), 1)
    print(f"x intercept = intercept/slope: {-intercept/slope:.2f} V")
Beta = 2* s[k]**2
print(f"Beta: {Beta:.4f}")
