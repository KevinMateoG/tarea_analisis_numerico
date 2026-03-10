import sympy as sp

x=sp.symbols('x')

import sympy as sp

def Newton(f,x0,tol):
  df = sp.diff(f,x)
  newton = x-f/df
  n = 0
  error = 1
  while error > tol:
    n += 1
    x1 = sp.lambdify(x,newton)(x0) #newton.subs(x,x0)
    error=abs(x1-x0)
    x0 = x1
    print(x0)
    if n == 20:
       break
  return float(x1), n

def Secante(f,x0,x1,tol):
    error = 1
    while error > tol:
        x2 = x1 -f(x1)*(x1-x0)/(f(x1)-f(x0))
        error = abs(x2-x1)
        x0 = x1
        x1 = x2
    return x2

def biseccion(f,a,b,tol=10**-2):
    contador = 0
    if f(a)*f(b) > 0:
        print("caho no hay nada que ver")
    else:
        while abs(b-a)>tol:
            contador += 1
            p = (a+b)/2
            if abs(f(p)) < tol:
                #print(p, contador)
                return p, contador
            if f(a)*f(p) < 0:
                b = p
            else:
                a = p
        #print(f"la solucion de la funcion: {p} {contador}")
    return p, contador

def pos_falsa(f,a,b,error):
  count = 0
  if f(a)*f(b) > 0:
    return
  else:
    p = b - f(b) * (a-b)/(f(a)-f(b))
    while abs(f(p)) > error:
      count += 1
      p = b - f(b) * (a-b)/(f(a)-f(b))
      if abs(f(p)) < error:
        break
      print(f"este es para la iteracion {count}: {p}")
      if f(a)*f(p) < 0:
        b=p
      else:
        a=p
    return p,count