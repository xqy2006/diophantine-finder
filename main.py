from sage.all import *
from fractions import Fraction

def multiply_list_values_1(lst, number):
    for i in range(len(lst)):
        lst[i] = lst[i] * number
    return lst
R = RationalField()
n = 200
#print(n)
P2 = ProjectiveSpace(2, R)
x, y, z = P2.coordinate_ring().gens()

#C = Curve(x**3 - (n-1)*x**2*y - (n-1)*x**2*z - (n-1)*x*y**2 - (2*n-3)*x*y*z - (n-1)*x*z**2 + y**3 - (n-1)*y**2*z - (n-1)*y*z**2 + z**3)

#Pt = [(w**2+1)*(3*w**3+8*w**2+14*w+11),-(w**2+2*w+2)*(3*w**3+w**2+7*w-2),w**6+3*w**5+11*w**4+17*w**3+20*w**2+12*w-1]

E = EllipticCurve_from_cubic(x**3 - (n-1)*x**2*y - (n-1)*x**2*z - (n-1)*x*y**2 - (2*n-3)*x*y*z - (n-1)*x*z**2 + y**3 - (n-1)*y**2*z - (n-1)*y*z**2 + z**3)
#print(E)
g = E.inverse()
print(E.codomain().integral_points(both_signs=True))
Pt = g(E.codomain().integral_points(both_signs=True)[0])


for n in range(1, 100000000000000000000000000000000000000000000000000000000000000001):

    nPt_inE = E(Pt)*n

    nPt_inC = g(nPt_inE)
    #print(nPt_inC)

    X = nPt_inC[0].numerator()
    Y = nPt_inC[1].numerator()
    Z = nPt_inC[0].denominator()
    


    if X > 0 and Y > 0:
        print("X =", X)
        print("Y =", Y)
        print("Z =", Z)
        #print("GOT IT!!! x=apple, y=banana, z=pineapple, check the above solution")
        break
    #else:
        #print("Nee, some coordinate was negative above, I keep in the loop\n")

# 在原始问题上评估点
problem = ((x/(y+z) + y/(x+z) + z/(x+y))-4)
#print(problem(X, Y, Z))
if problem(X, Y, Z) == 0:
    print("I evaluated the point to the original problem and yes, it worked!")
#else:
    #print("Mmm this cannot happen!")
