from Waves import *

# === PARÁMETROS ===
E_0 = 100  # V/m
LAMBDA_VAC = 1310E-9
H = 40E-6
X = 20E-2
N0 = 1.338 + 1j*1.71E-04
N2 = 1.340 + 1j*1.71E-04
L = 1.65E-3
delta = 1.338-1.340

# === SIMULACIÓN CON Δn = 0.002 ===
ray_ref = LinearEWave(E_0, LAMBDA_VAC, N0)
ray_2 = LinearEWave(E_0, LAMBDA_VAC, N2)

ray_ref.propagate(L)
ray_2.propagate(L)

ray_ref.newmed(1)
ray_2.newmed(1)

Ymax = 23E-3
Ymin = -23E-3
space = np.linspace(Ymin, Ymax, 1000)
Iq_diff = []
y0 = (X*L/H)*delta
print(f"corrimiento de la franja:{y0}m")


for y in space:
    dref = dr(X, y, H)
    d2 = dd(X, y, H)
    ray_ref.propagate(dref)
    ray_2.propagate(d2)
    Iq_diff.append(ray_ref.interference(ray_2))
    ray_ref.devolve()
    ray_2.devolve()

# === SIMULACIÓN CON N0 = N2 ===
ray1_equal = LinearEWave(E_0, LAMBDA_VAC, N0)
ray2_equal = LinearEWave(E_0, LAMBDA_VAC, N0)

ray1_equal.propagate(L)
ray2_equal.propagate(L)

ray1_equal.newmed(1)
ray2_equal.newmed(1)

Iq_equal = []

for y in space:
    dref = dr(X, y, H)
    d2 = dd(X, y, H)
    ray1_equal.propagate(dref)
    ray2_equal.propagate(d2)
    Iq_equal.append(ray1_equal.interference(ray2_equal))
    ray1_equal.devolve()
    ray2_equal.devolve()

# === GRAFICAR AMBOS CASOS ===
rcParams.update({
    "text.usetex": True,           # Usa LaTeX para texto
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9
})

plt.figure(figsize=(3.4, 2.5))  # Tamaño típico de columna en paper (~8.6 cm)
plt.plot(space, Iq_diff, color='#1f77b4', lw=1.2)
plt.plot(space, Iq_equal, color='#e15759', lw=1.2)

plt.axvline(x=0, color='black', linestyle='--', lw=1)
plt.axvline(x=y0, color='black', linestyle=':', lw=1)

plt.xlabel(r'$y$ [m]')
plt.ylabel(r'Irradiancia [W/m$^2$]')

plt.tight_layout(pad=0.5)
plt.savefig("interferencia_paper.pdf", dpi=300)  # Opcional: guardar como PDF
plt.show()
