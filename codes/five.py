#import sympy
from sympy import *
T,t,t1,t2= symbols('T t t1 t2')
exp = 1/T
intr = integrate(exp, (t, t1, t2))
print(format(intr))
