from ceros_de_funcion import *

#Metodo biseccion

f= lambda s: (s**4) + (20.75) * s**3 + (92.6) * s**2 + (73.69) * s

print(biseccion(f, -2, 0,1e-4))