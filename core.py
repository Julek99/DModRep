from sympy import *

class representation:
    def __init__(self, nb, crd, bases, chart = 0):
        self.cfs = {}
        self.crd = crd
        self.twist = symbols("\lambda")-1
        self.chart = chart
        self.bases = bases
        self.nb = nb

    def nabla(self, x):
       # print(diff(x,self.crd))
        #print(self.nb*x)
        return diff(x,self.crd) - self.nb*x

    def H(self, x):
        if self.chart == 0:
            return apart(2*self.crd*self.nabla(x) - self.twist*x, self.crd)
        elif self.chart == 1:
            return apart(-2*self.crd*self.nabla(x) + self.twist*x, self.crd)
        else:
            raise Exception("No such chart.")

    def F(self,x):
        if self.chart == 1:
            return apart(self.crd**2*self.nabla(x) - self.crd*self.twist*x, self.crd)
        elif self.chart == 0:
            return apart(-self.nabla(x), self.crd)
        else:
            raise Exception("No such chart.")

    def E(self,x):
        if self.chart == 0:
            return apart(self.crd**2*self.nabla(x) - self.crd*self.twist*x, self.crd)
        elif self.chart == 1:
            return apart(-self.nabla(x), self.crd)
        else:
            raise Exception("No such chart.")

    def custom(self, txt, x):
        txt = txt.replace("H", "self.H(x)")
        txt = txt.replace("E", "self.E(x)")
        txt = txt.replace("F", "self.F(x)")
        ans = eval(txt)
        return collect(ans, self.crd)

    def compute(self,txt,mx):
        print("The sl_2-element A = " + txt + " acts on this connection as: ")
        print()
        out = 'A * 1 = '+ str(self.custom(txt,1))
        print(out.replace('**','^'))
        for b in self.bases:
            for i in range(1,mx+1):
                out = 'A * (' + str(b) + ')^' + str(i) \
                      + ' = '+ str(self.custom(txt,b**i))
                print(out.replace('**','^'))
        print()
        
    def calc_letter(self, txt, mx):
        CFS = {}
        for n in range(mx+1):
            pol = poly(self.custom(txt,self.bases[0]**n),self.crd)
            cfs = {}
            for m in range(mx+1):
                cf = pol.coeff_monomial(self.crd**m)
                if cf != 0:
                    cfs[m] = cf
                CFS[n] = cfs
        return CFS
    
    def draw(self, letter, mx):
        out = "\\[ \\begin{tikzcd}\n"
        cfs = self.calc_letter(letter, mx)
        for n in range(mx+1):
            if n == 0:
                out += " 1 "
            else:
                out += "(" + str(self.bases[0]) + ")^{" + str(n) + "} "
                     
            for m in cfs[n].keys():
                d = n-m
                
                if d > 0:
                    out += " \\arrow[" + "l"*abs(d) + ","
                    out += "bend right = " + str(abs(30*(abs(d)-1)))
                    out += ",\"{" + str(cfs[n][m]) + "}\"]"
                    
                elif d < 0:
                    out += " \\arrow["+ "r"*abs(d) + ","
                    out += "bend right = " + str(abs(30*(abs(d)-1)))
                    out += ",\"{" + str(cfs[n][m]) + "}\"]"
                
                else:
                    out += " \\arrow[ loop above,"
                    out += "\"{" + str(cfs[n][m]) + "}\"]"
                        
            if n != mx:
                out += " & \n"

        out +="\n\\end{tikzcd}\\]"
        out = out.replace("**","^")
        return out.replace("*","")
    
