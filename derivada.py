from sympy import *
x=symbols('x')


n=input('da el grado de la derivada')
fun=(x**2-1)**float(n)
derivada2=diff(fun,x,n).subs(x,0)

print(derivada2)


	
