import sympy as sy
from sympy.matrices import Matrix

c0,c1,c2,c3,s0,s1,s2,s3 = sy.symbols('c0 c1 c2 c3 s0 s1 s2 s3')

l1x,l1z,l2x,l2y,l2z,l3x,l3y = sy.symbols('l1x l1y l2x l2y l2z l3x l3y')

l3z,l4x,l4y,l4z,l5x,l5z = sy.symbols('l3z l4x l4y l4z l5x l5z')


T0_1 = Matrix(([c0, 0, s0, l1x],
             [0, 1, 0, 0],
             [-s0, 0, c0, l1z],
             [0, 0, 0, 1]))

T1_2 = Matrix(([1, 0, 0, l2x],
               [0, c1, -s1, l2y],
               [0, s1, c1, l2z],
               [0, 0, 0, 1]))
                 
T2_3 = Matrix(([c2, 0, s2, l3x],
               [0, 1, 0, l3y],
               [-s2, 0, c2, l3z],
               [0, 0, 0, 1]))
                 
T3_4 = Matrix(([c3, -s3, 0, l4x],
               [s3, c3, 0, l4y],
               [0, 0, 1, l4z],
               [0, 0, 0, 1]))

T4_5 = Matrix(([1, 0, 0, l5x],
               [0, 1, 0, 0],
               [0, 0, 1, l5z],
               [0, 0, 0, 1]))

#T1 = T0_1.dot(T1_2)
T5_0 = T0_1*T1_2*T2_3*T3_4*T4_5
'''          
a = Matrix(([2,3],[1,5]))
b = Matrix(([9,2],[5,3]))

c = a.dot(b)
d = a*b
'''
print("\nm00 = ", T5_0[0,0])
print("\nm01 = ", T5_0[0,1])
print("\nm02 = ", T5_0[0,2])
print("\nm03 = ", T5_0[0,3])
print("\nm10 = ", T5_0[1,0])
print("\nm11 = ", T5_0[1,1])
print("\nm12 = ", T5_0[1,2])
print("\nm13 = ", T5_0[1,3])
print("\nm20 = ", T5_0[2,0])
print("\nm21 = ", T5_0[2,1])
print("\nm22 = ", T5_0[2,2])
print("\nm23 = ", T5_0[2,3])
print("\nm30 = ", T5_0[3,0])
print("\nm31 = ", T5_0[3,1])
print("\nm32 = ", T5_0[3,2])
print("\nm33 = ", T5_0[3,3])




