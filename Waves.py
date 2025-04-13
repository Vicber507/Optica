import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0
from matplotlib import rcParams

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

