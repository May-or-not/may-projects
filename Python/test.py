import numpy as np
import matplotlib.pyplot as plt

#Este código realiza la impresión de tu primer hola mundo
print("Hola Mundo")

x = np.linspace(10, 20, 50)
y = np.linspace(90, 100, 50)

plt.figure(1, edgecolor='r')
plt.plot(x,y, color = 'k')
plt.show()