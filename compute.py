from sympy import *
from time import *
from core import *

def inpt(txt):
    ans = input(txt)
    if ans == "#":
        quit()
    return ans


print("Welcome to the Beilinson-Bernstein localisation calculator. This is a tool for " +\
      "the computation of sl_2-representations which correspond to O-coherent D-modules"+\
      "on the flag variety of sl_2, that is, the complex projective plane X = CP^1.")
print("Here, D denotes the sheaf (of rings) of twisted differential operators, with twist" + \
      "given by λ-1 for λ a dominant integral weight.")
print("Currently, this tool only supports work local work in one of the two charts " +\
      "U_0 = X \\ {inf} and U_inf = X \\ {0}.")

# Input the chart

while True:
    chart = inpt("\nTo start, please specify the chart you'd like to work in. " \
              + "\nFor the chart U_0, type \"0\". For the chart U_inf, " \
                  + "type \"inf\".\nTo quit, type \"#\". \n \n")
    if chart == "0":
        print("\nYou have chosen the chart U_0. The coordinate on this chart " + \
              "is denoted as \"z\".\nPlease do not use \"z\" as a variable name.")
        z = symbols('z')
        crd = z
        chart = 0
        break
    elif chart == "inf":
        print("\nYou have chosen the chart U_inf. The coordinate on this chart " + \
              "is denoted as \"w\".\nPlease do not use \"w\" as a variable name.")
        w = symbols('w')
        crd = w
        chart = 1
        break
    else:
        print("\nInvalid input. Please try again.\n ")

# Input the twist

'''
while True:
    print("\nNow please specify the twist λ-ρ, where ρ = 1 is the " \
          + "Weyl element (so that λ = ρ = 1 corresponds to the" + \
          "untwisted sheaf). \nTo quit, type \"#\". \n \n")
    twist = inpt("λ = ")
    try:
        twist = int(twist)-1
        break
    except ValueError as e:
        print("The twist must be a dominant integral weight of sl_2."+ \
              "Please eneter a positive integer for λ.")
'''
            
# Input the variables

first = True
ls = []
while True:
    if first:
        smbn = inpt("\nNow, please specify any variables you'd like to use." \
                     + "\nTo continue without variables, simply press ENTER." \
                     + "\nPlease type in a variable name. To quit, type \"#\".\n\n")
        first = False
    else:
         smbn = inpt("\nWould you like to specify another variable? \nIf yes, simply type" \
          + " in the next variable name. If not, press ENTER. \nTo quit, type \"#\".\n\n")
    if smbn == "":
        break
    elif(smbn == "z"):
        print("\nPlease do not use the coordinate map as a variable name.")
        continue
    
    smb = inpt("\nPlease type in the variable description for the variable \"" \
              + smbn + \
                "\" in LaTeX notation. \n To quit, type \"#\". \n \n")
    print("\nVariable \"" + smbn + "\" initialised successfully as \""+ smb + "\".")
    exec(smbn + "= symbols(\'" + smb.replace("\\", "\\\\") + "\')")
    ls.append(eval(smbn))

# Input the bases

bases = []
first = True
while True:
    if first:
        b = inpt("Now, please specify the bases you'd like to use.\nNote: " + \
                     "specifying a basis element automatically includes all its powers. " \
                  + "\nPlease type in a basis element in terms of the coordinate " + \
                     str(crd) + ". To quit, type \"#\".\n\n")
        first = false
    else:
        b = inpt("\nWould you like to specify another basis element? \nIf yes, simply type" \
          + " it in. If not, press ENTER. \nTo quit, type \"#\".\n\n")
        if b == "":
            break
    bases.append(eval(b))

# Input the connection

nb_txt = inpt("Finally, please specify the connection ∇ you'd like to compute, " + \
           "in terms of the coordinate " + str(crd) + ".\nYou may use any defined" + \
           " variables by their names. To quit, type \"#\".\n\n∇ = d - ")
nb = eval(nb_txt)

print("\nComputing representation...")

rep = representation(nb, crd, bases, chart = chart)
sleep(2)

first = True
while True:
    if first:
        print("Representation computed.\n\nTo display the action of an element A of sl_2 on the" + \
              " local sections of this module, please type A in terms of the basis {E,F,H} of sl_2." + \
              "\nTo quit, type \"#\". \n")
        A = inpt("A = ")
        first = False
    else:
        print("Would you like to compute the action of another element? If yes, simply type it in.")
        print("If not, press ENTER.")
        A = inpt("A = ")
        if A == "":
            print("\nThank you for using the Beilinson-Bernstein localisation calculator. " + \
                  "Have a nice day!")
            break
    print("\nOn how many powers of the bases would you like to compute the action of A?" + \
          "\nTo quit, type \"#\". \n")
    mx = inpt("n = ")
    print()
    try:
        rep.compute(A,int(mx))
    except Exception as e:
        print("Something went wrong.")
        print("Make sure that your expression for A contains only elements of the sl_2-basis {E,F,H} "+\
              "and their combinations via addition, subtraction and multiplication. Also make sure that all "+\
              "multiplication is written using the symbol \"*\" and that your input for n is a positive integer.")

