from Waves import *
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Parámetros
A1, A2 = 1.0, 1.0
lamb_emitted = 500e-8
n = 1.5 + 0j

# Crear ondas
wave1 = RadialWave(A1, 500e-8, n, x0=-8e-6, y0=0, phase=180)
wave2 = RadialWave(A2, lamb_emitted, n, x0=8e-6, y0=0)

# Malla espacial (en micrómetros)
x = np.linspace(-20e-6, 20e-6, 200)
y = np.linspace(-20e-6, 20e-6, 200)
X, Y = np.meshgrid(x, y)

# Superposición
E_x, E_y = wave1.superposition(wave2, X, Y, t=0)

E_total = np.sqrt(E_x**2 + E_y**2)



# Visualizar el campo total
plt.imshow(E_total, extent=(-10, 10, -10, 10), origin='lower', cmap='viridis')
plt.colorbar(label='Magnitud del campo eléctrico')
plt.title('Campo eléctrico resultante por superposición de dos ondas')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Configurar la figura
fig, ax = plt.subplots(figsize=(10, 8))
img = ax.imshow(np.zeros_like(X), extent=(-10, 10, -10, 10),vmin=0,vmax=1.2,
                origin='lower', cmap='viridis')
plt.colorbar(img, label='Magnitud del campo eléctrico')
ax.set_title('Evolución temporal del campo eléctrico')
ax.set_xlabel('x (μm)')
ax.set_ylabel('y (μm)')

# Función de inicialización
def init():
    img.set_array(np.zeros_like(X))
    return [img]

# Función de animación
def update(frame):
    # Calculamos el tiempo en segundos (ajusta este factor según necesites)
    t = frame * 1e-15
    
    # Calculamos el campo en este instante
    E_x, E_y = wave1.superposition(wave2, X, Y, t)
    E_total = np.sqrt(E_x**2 + E_y**2)
    
    
    # Actualizamos la imagen
    img.set_array(E_total)
    ax.set_title(f'Campo eléctrico en t = {t:.2e} s')
    
    return [img]

# Crear la animación
ani = FuncAnimation(fig, update, frames=60, init_func=init,
                    blit=True, interval=30)

plt.tight_layout()
plt.show()

