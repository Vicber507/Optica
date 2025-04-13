import numpy as np
from Waves import *

def Mphase(theta,d,lamb):
   return (2*np.pi/lamb)*(2*d*np.cos(theta) + lamb/2)


r1 = LinearEWave(10,1310E-8,1,Mphase(0,0.001,1310E-9))
r2 = LinearEWave(10,1310E-8,1,0)



Ymax = 12E-05
Ymin = -12E-05
space = np.linspace(Ymin, Ymax, 1000)
MicY = []


for y in space:
    dref = dr(75E-03,y,50E-03)
    d2 = dd(75E-03,y,50E-03)
    r1.propagate(dref)
    r2.propagate(d2)
    MicY.append(r1.interference(r2))
    r1.devolve()
    r2.devolve()
    
    
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
plt.plot(space, MicY, color='#1f77b4', lw=1.2)


plt.xlabel(r'$y$ [m]')
plt.ylabel(r'Irradiancia [W/m$^2$]')

plt.tight_layout(pad=0.5)
plt.savefig("interferencia_paper_michelson.pdf", dpi=300)  # Opcional: guardar como PDF
plt.show()
