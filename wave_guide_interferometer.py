######################################
# Simulacion de un interferometro    #
# de guia de onda con fase adquirida #
# por medios distintos               #
######################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0

def dr(x, y, h):
    return np.sqrt(x**2 + (y - (h / 2))**2)

def dd(x, y, h):
    return np.sqrt(x**2 + (y + (h / 2))**2)

class LinearEWave():
    def __init__(self,A,lamb,n, phase = 0):
        self.amp = A
        self.n = n
        self.nr = np.real(self.n)
        self.nc = np.imag(self.n)
        self.lamb = lamb
        self.k = 2*np.pi/self.lamb
        self.w = c*self.k/self.nr 
        self.alpha = self.w* self.nc/c
        self.phase = phase
        
    def evolve(self,distance):
        phi = self.k*distance
        amp = self.amp*np.exp(-self.alpha*distance)
        self.phase += phi
        self.amp = amp
    
    def devolve(self,distance):
        phi = self.k*distance
        amp = self.amp*np.exp(self.alpha*distance)
        self.phase -= phi
        self.amp = amp
        
    def newmed(self,n):
        self.n = n
        self.lamb = c*2*np.pi/(np.real(n)*self.w)
         
    def phase_dif(self,wave2):
            delta = self.phase - wave2.phase 
            return delta
        
    def interference(self,wave2):
        const = 0.5*epsilon_0*c
        return const*(self.amp**2 + wave2.amp**2 + 2*self.amp*wave2.amp*np.cos(self.phase_dif(wave2)))
        
    

