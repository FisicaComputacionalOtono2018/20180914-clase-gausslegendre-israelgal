import math 
from sympy import *
x=symbols('x')

def factorial(n):
    M=1
    F=1
    while M<float(n):
        M=M+1
        F=F*M
    return (F)
    
n=input('da el grado de la derivada')
r=input('dame un numero x')

fun=(x**2-1)**float(n)
derivada=diff(fun,x,n)
xevaluado=derivada.subs(x,float(r))


polinomio=(1/(2**float(n)*factorial(n)))*derivada


print(factorial(n))
print(derivada)
print(xevaluado)
print(polinomio)
