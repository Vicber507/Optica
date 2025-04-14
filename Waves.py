import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0
from scipy.special import j0
from matplotlib import rcParams
from scipy.ndimage import gaussian_filter


def dr(x, y, h):
    return np.sqrt(x**2 + (y - h/2)**2)

def dd(x, y, h):
    return np.sqrt(x**2 + (y + h/2)**2)

class LinearEWave:
    def __init__(self, A, lamb_emitted, n, phase=0):
        self.amp = A
        self.lamb0 = lamb_emitted
        self.omega = (2 * np.pi * c) / self.lamb0
        self.n = n
        self.nr = np.real(n)
        self.nc = np.imag(n)
        self.k = (2 * np.pi / self.lamb0) * self.nr
        self.alpha = (2 * np.pi / self.lamb0) * self.nc
        self.phase = phase
        self.preamp = A
        self.prephase = phase

    def update_constants(self):
        self.nr = np.real(self.n)
        self.nc = np.imag(self.n)
        self.k = (2 * np.pi / self.lamb0) * self.nr
        self.alpha = (2 * np.pi / self.lamb0) * self.nc

    def propagate(self, dx, dt=0):
        self.preamp = self.amp
        self.prephase = self.phase
        self.amp *= np.exp(-self.alpha * dx)
        self.phase += self.k * dx - self.omega * dt

    def devolve(self):
        self.amp = self.preamp
        self.phase = self.prephase

    def phase_dif(self, wave2):
        return self.phase - wave2.phase

    def newmed(self, n):
        self.n = n
        self.update_constants()

    def interference(self, wave2):
        const = 0.5 * epsilon_0 * c * self.nr
        return const * (self.amp**2 + wave2.amp**2 + 2 * self.amp * wave2.amp * np.cos(self.phase_dif(wave2)))


class RadialWave: 
    def __init__(self, A, lamb_emitted, n, x0,y0,phase=0):
        self.amp = A
        self.x0 = x0
        self.y0 = y0
        self.lamb0 = lamb_emitted
        self.omega = (2 * np.pi * c) / self.lamb0
        self.n = n
        self.nr = np.real(n)
        self.nc = np.imag(n)
        self.k = (2 * np.pi / self.lamb0) * self.nr
        self.alpha = (2 * np.pi / self.lamb0) * self.nc
        self.phase = phase*np.pi/180

    
    def propagate(self, x, y, t=None):
        x = x + self.x0
        y = y + self.y0
        r = np.sqrt(x**2 + y**2)
        r_hat_x = np.where(r != 0, x / r, 0)
        r_hat_y = np.where(r != 0, y / r, 0)

        if t is None:
            t = r / (c / self.nr)  
        
        E_scalar = self.amp * np.exp(-self.alpha*r)*j0(self.k * r) * np.cos(-self.omega * t + self.k * r + self.phase)

        # Componentes cartesianas del campo
        E_x = E_scalar * r_hat_x
        E_y = E_scalar * r_hat_y

        return E_x, E_y
    
    
    def superposition(self, wave2, x, y, t=None):
        E1_x, E1_y = self.propagate(x, y, t)
        E2_x, E2_y = wave2.propagate(x, y, t)
        E_x = E1_x + E2_x
        E_y = E1_y + E2_y
        return E_x, E_y

        
    