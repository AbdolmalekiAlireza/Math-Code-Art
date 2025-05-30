import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(xmin, xmax, ymin, ymax, width, height, maxtier):
    xs = np.linspace(xmin, xmax, width)
    ys = np.linspace(ymin, ymax, height)
    fractal = np.empty((width, height))

    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            c = x + 1j * y
            z = 0
            for k in range(maxiter):
                z = z * z + c
                if abs(z) > 2:
                    break
            fractal[i, j] = k
    return fractal
                
# Parameters
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 1800, 1800
maxiter = 80

data = mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter)

plt.figure(figsize=(6, 6),  dpi=1000)
plt.imshow(data.T, extent=[xmin, xmax, ymin, ymax])
plt.axis('off')
plt.tight_layout()
plt.show()
