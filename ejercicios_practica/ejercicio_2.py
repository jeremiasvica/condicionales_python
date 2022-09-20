# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('el texto mayor es', texto_1)
elif texto_2 > texto_1:
    print('el texto mayor es', texto_2)
else:
    print('iguales')

cant_1 = len(texto_1)
cant_2 = len(texto_2)
if cant_1 > cant_2:
    print(texto_1, 'tiene mas letras que', texto_2)
elif cant_2 > cant_1:
    print(texto_2, 'es mayor en letras que', texto_1)
else:
    print('igual longitud')

if texto_1[0] > texto_2[0]:
    print('primer caracter mayor de', texto_1)
elif texto_2[0] > texto_1[0]:
    print('primer caracter mayor de', texto_2)
else:
    print('son iguales')

if copia_texto_1 == texto_1:
    print(copia_texto_1, 'es igual a', texto_1)
else:
    print(copia_texto_1, 'y', texto_1, 'no son iguales')

if copia_texto_1 != texto_2:
    print(copia_texto_1, 'no es igual a', texto_2)
else:
    print(copia_texto_1, 'es igual a', texto_2)


