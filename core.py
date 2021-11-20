from sympy import *
import os
z,a,b,l = symbols('z \\alpha \\beta \lambda')
w = 1/z

class representation:
    def __init__(self, chart = 0, twist = 0, bases = [z,1/z,1/(z-1)], mx = 5):
        self.cfs = {}
        self.chart = chart
        self.twist = twist
        self.mx = mx
        self.bases = bases

    def nabla(self, x):
        if self.chart == 0:
            return diff(x,z) - a*x/z - b*x/(z-1)
        else:
            return diff(x,w)

    def H(self, x):
        if self.chart == 0:
            return apart(2*z*self.nabla(x) - self.twist, z)
        elif self.chart == 1:
            return apart(-2*w*self.nabla(x) + self.twist, w)
        else:
            raise Exception("No such chart.")

    def F(self,x):
        if self.chart == 1:
            return apart(w**2*self.nabla(x) - w*self.twist, w)
        elif self.chart == 0:
            return apart(-self.nabla(x), z)
        else:
            raise Exception("No such chart.")

    def E(self,x):
        if self.chart == 0:
            return apart(z**2*self.nabla(x) - z*self.twist, z)
        elif self.chart == 1:
            return apart(-self.nabla(x), w)
        else:
            raise Exception("No such chart.")
        
    def X(self,x):
        if self.chart == 0:
            return apart(0.5*self.H(x)+self.F(x), z)
        elif self.chart == 1:
            return apart((1/2)**self.H(x)+self.F(x), w)
        else:
            raise Exception("No such chart.")

    def compute(self,fn, pt=False):
        print("The sl2-element " + fn.__name__ + " acts on this connection as: ")
        print()
        for b in self.bases:
            for i in range(self.mx):
                out = fn.__name__ + ' * (' + str(b) + ')^' + str(i) \
                      + ' = '+ str(fn(b**i))
                print(out.replace('**','^'))
        print()
