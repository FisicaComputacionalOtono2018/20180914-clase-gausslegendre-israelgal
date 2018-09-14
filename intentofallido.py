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
valordex=input('dame un numero x')

fun=(x**2-1)**float(n)
derivada=diff(fun,x,n)
libres={"x":valordex}
print(eval(derivada,{},libres))

#evaluar=diff(fun,x,n).subs(x,valordex)

#polinomio=(1/(2**float(n)*factorial(n)))*evaluar

print(factorial(n))
print(derivada)
#print(evaluar)
 
#print(polinomio.evalf(x))

