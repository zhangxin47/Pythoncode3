import numpy as np
import matplotlib.pyplot as py
from sympy import diff, symbols , integrate, var ,simplify , together , solve
# x, y , z = symbols("x,y,z")
# c=diff(x**2+2*x+1 , x)
# print(c)
# d = integrate(c,y)
# print(d)
""" 
Notation Definition
Q  : the quantity which manufacturer want to order; a decision variable
D1 & D2 : the market demand of High-end and Low-end product; a random variable 
P1 & P2 : the price of High-end and Low-end product
M1 & M2 : the production cost of High-end and Low-end product
R1      : the reserve price of buying raw materials
C1      : the wholesale price of raw materials
C2      : the purchase price of recycled materials
Ce      : the emerency order price of raw materials
S1      : the salvage value of raw materials
"""
# Model1: Pure model
## Wholesale 批發型
P1 , M1 , D1 , P2, D2, M2, C1, Ce, S1, L = symbols ("P1 , M1 , D1 , P2, D2, M2, C1, Ce, S1, L", real = True)
Q = symbols("Q",real = True)
profitV1Term1 = (P1 - M1) * D1 + (P2*D2 - M2*D2) - Q * C1 - (D1 + D2 - Q) * Ce
profitV1Term2 = (P1 - M1) * D1 + (P2*D2 - M2*D2) - Q * C1 + (Q - D1 - D2) * S1
WpiMV2a = integrate(integrate(profitV1Term1/(L**2),(D2,Q-D1,L)),(D1,0,Q)) \
    + integrate(integrate(profitV1Term1/(L**2),(D2,0,L)),(D1,Q,L)) \
        + integrate(integrate(profitV1Term2/(L**2),(D2,0,Q-D1)),(D1,0,Q))
print(simplify(WpiMV2a))
print(simplify(diff(WpiMV2a,Q,2)))
print(solve(diff(WpiMV2a,Q,1), Q , real = True))