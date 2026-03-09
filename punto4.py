from ceros_de_funcion import *
import numpy as np
import matplotlib.pyplot as plt
#Metodo biseccion

f= lambda s: (s**4) + (20.75) * s**3 + (92.6) * s**2 + (73.69) * s

ux = np.linspace(0,10,100)
plt.plot(ux, f(ux))
plt.axhline(0,linestyle="--", color='red')