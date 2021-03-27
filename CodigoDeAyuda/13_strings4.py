cadena = "Hola {}"
cadena.format("jorge")
print(cadena)#nos imprime "Hola {}" porque no lo guardamos ni nada
cadena = cadena.format("jorge")
print(cadena)#"Hola jorge"