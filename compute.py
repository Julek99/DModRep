import core
from sympy import *
from time import *

# Input the chart

while True:
    chart = input("\nTo start, please specify the chart you'd like to work in. " \
              + "\nFor the chart U_0, type \"0\". For the chart U_inf, " \
                  + " type and \"1\".\nTo quit, type \"#\". \n \n")
    if chart == "0":
        print("\nYou have chosen the chart U_0. The coordinate on this chart " + \
              "is denoted as \"z\".\nPlease do not use \"z\" as a variable name.")
        z = symbols('z')
        crd = z
        break
    elif chart == "1":
        print("\nYou have chosen the chart U_inf. The coordinate on this chart " + \
              "is denoted as \"w\".\nPlease do not use \"w\" as a variable name.")
        w = symbols('w')
        crd = w
        break
    elif chart == "#":
        quit()
    else:
        print("\nInvalid input. Please try again.\n ")
            
# Input the variables

first = True
ls = []
while True:
    if first:
        smbn = input("\nNow, please specify any variables you'd like to use." \
                     + "\nTo continue without variables, simply type \"-\"." \
                     + "\nPlease type in a variable name. To quit, type \"#\".\n\n")
        first = False
    else:
         smbn = input("\nWould you like to specify another variable? \nIf yes, simply type" \
          + " in the next variable name. If not, type \"-\". \nTo quit, type \"#\".\n\n")
    if smbn == "#":
        quit()
    elif smbn == "-":
        break
    
    smb = input("\nPlease type in the variable description for the variable \"" \
              + smbn + \
                "\". in LaTeX notation. \n To quit, type \"#\". \n \n")
    if smb == "#":
        quit()
    print("\nVariable \"" + smbn + "\" initialised successfully as \""+ smb + "\".")
    exec(smbn + " = symbols(\'" + smb.replace("\\", "\\\\") + "\')")
    exec("ls.append(" + smbn + ")")

# Input the bases

bases = []
first = True
while True:
    if first:
        b = input("\nNow, please specify bases you'd like to use.\nNote: " + \
                     "specifying a basis element automatically includes all its powers. " \
                  + "\nPlease type in a basis element in terms of the coordinate " + \
                     str(crd) + ". To quit, type \"#\".\n\n")
        first = false
    else:
        b = input("\nWould you like to specify another basis element? \nIf yes, simply type" \
          + " it in. If not, type \"-\". \nTo quit, type \"#\".\n\n")
        if b == "-":
            break
    if b == "#":
        quit()

    exec("bases.append(" + b + ")")

# Input the connection

nb = input("Finally, please specify the connection \\nabla you'd like to compute, " + \
           "in terms of the coordinate " + str(crd) + ". You may use any defined" + \
           " variables by their names.\nTo quit, type \"#\".\n\n\\nabla = d - ")

if nb == "#":
        quit()

print("\nComputing representation...")
sleep(2)
print("Representation computed.")
