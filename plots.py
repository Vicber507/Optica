from wave_guide_interferometer import * 

#######################################
#        Confifuration constasnts     #    
#######################################

E_0 = 978 # V/m
LAMBDA_0 = 1310E-09 #wavelenght initial in meters^-1
H = 40E-06 #distance between rays in meters
X = 20E-2 #distance to the detector in meters
N0 = 1.338 + 1j*1.71E-04 #refraction index 0
N2 = 1.340 + 1j*1.71E-04 #refraction index 2
L = - 1.65E-03 #lenght of de tubes
W_0 = c*2*np.pi/(LAMBDA_0*np.real(N0))
LAMBDA_2 = c*2*np.pi/(np.real(N2)*W_0) #wavelenght initial in meters^-1


#######################################
#        Creatcion of wave an evol.   #    
#######################################

ray_ref = LinearEWave(E_0,LAMBDA_0,N0)
ray_2   = LinearEWave(E_0,LAMBDA_2,N2)

# we evolve the waves to the new medium
ray_ref.evolve(L)
ray_2.evolve(L)
ray_2.newmed(N0)

# Simulation (we will be constatly evolving and devolving waves and calcultate interference if
# thats the path)

Ymax = 30E-3
Ymin = -30E-3
space = np.linspace(Ymin, Ymax, 200)

Ir = []
for y in space:
    dref = dr(X,y,H)
    d2   = dd(X,y,H)
    ray_ref.evolve(dref)
    ray_2.evolve(d2)
    Ir.append(ray_ref.interference(ray_2))
    ray_ref.devolve(dref)
    ray_2.devolve(d2)



# Graficar ambas curvas en la misma figura
plt.plot(space,Ir, color='red',alpha = 1,ls = '-', label = r'$I(y) I_1 +I_2 + I_{int}$ para $\delta n = -0.002$')
plt.xlabel("Coordenada longitudinal de la pantalla [m]")
plt.ylabel("Irradianza [W/m²]")
plt.title("Irradianza vs posición para distintos índices $n_2$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



#######################################
#        Confifuration constasnts     #    
#######################################

E_0 = 978 # V/m
LAMBDA_0 = 1310E-09 #wavelenght initial in meters^-1
H = 40E-06 #distance between rays in meters
X = 20E-2 #distance to the detector in meters
N0 = 1.338 + 1j*1.71E-04 #refraction index 0
N2 = 1.338 + 1j*1.71E-04 #refraction index 2
L = - 1.65E-03 #lenght of de tubes
W_0 = c*2*np.pi/(LAMBDA_0*np.real(N0))
LAMBDA_2 = c*2*np.pi/(np.real(N2)*W_0) #wavelenght initial in meters^-1


#######################################
#        Creatcion of wave an evol.   #    
#######################################

ray_ref = LinearEWave(E_0,LAMBDA_0,N0)
ray_2   = LinearEWave(E_0,LAMBDA_2,N2)

# we evolve the waves to the new medium
ray_ref.evolve(L)
ray_2.evolve(L)
ray_2.newmed(N0)

# Simulation (we will be constatly evolving and devolving waves and calcultate interference if
# thats the path)

Ir = []
for y in space:
    dref = dr(X,y,H)
    d2   = dd(X,y,H)
    ray_ref.evolve(dref)
    ray_2.evolve(d2)
    Ir.append(ray_ref.interference(ray_2))
    ray_ref.devolve(dref)
    ray_2.devolve(d2)



# Graficar ambas curvas en la misma figura
plt.plot(space,Ir, color='green',alpha = 1,ls = '-', label = r'$I(y) I_1 +I_2 + I_{int}$ para $\delta n = 0$')
plt.xlabel("Coordenada longitudinal de la pantalla [m]")
plt.ylabel("Irradianza [W/m²]")
plt.title("Irradianza vs posición para distintos índices $n_2$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




#######################################
#        Confifuration constasnts     #    
#######################################

E_0 = 978 # V/m
LAMBDA_0 = 1310E-09 #wavelenght initial in meters^-1
H = 40E-06 #distance between rays in meters
X = 20E-2 #distance to the detector in meters
N0 = 1.340 + 1j*1.71E-04 #refraction index 0
N2 = 1.338 + 1j*1.71E-04 #refraction index 2
L = - 1.65E-03 #lenght of de tubes
W_0 = c*2*np.pi/(LAMBDA_0*np.real(N0))
LAMBDA_2 = c*2*np.pi/(np.real(N2)*W_0) #wavelenght initial in meters^-1


#######################################
#        Creatcion of wave an evol.   #    
#######################################

ray_ref = LinearEWave(E_0,LAMBDA_0,N0)
ray_2   = LinearEWave(E_0,LAMBDA_2,N2)

# we evolve the waves to the new medium
ray_ref.evolve(L)
ray_2.evolve(L)
ray_2.newmed(N0)

# Simulation (we will be constatly evolving and devolving waves and calcultate interference if
# thats the path)


Ir = []
for y in space:
    dref = dr(X,y,H)
    d2   = dd(X,y,H)
    ray_ref.evolve(dref)
    ray_2.evolve(d2)
    Ir.append(ray_ref.interference(ray_2))
    ray_ref.devolve(dref)
    ray_2.devolve(d2)



# Graficar ambas curvas en la misma figura
plt.plot(space,Ir, color='blue',alpha = 1,ls = '-', label = r'$I(y) I_1 +I_2 + I_{int}$ para $\delta n = 0.002$')
plt.xlabel("Coordenada longitudinal de la pantalla [m]")
plt.ylabel("Irradianza [W/m²]")
plt.title("Irradianza vs posición para distintos índices $n_2$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()