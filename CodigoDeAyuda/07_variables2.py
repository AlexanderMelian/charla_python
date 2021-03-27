vGlobal = "Variable str Global"
def funcion():
    vLocal = "Variable str local"
    print(vLocal)# Variable str local

print(vGlobal)# Variable str Global
funcion()# Vamos a la funcion 'funcion'

#print(vLocal)   Si tratamos de ejecutar este comando fuera de la funcion saldra "NameError: name 'vLocal' is not defined"