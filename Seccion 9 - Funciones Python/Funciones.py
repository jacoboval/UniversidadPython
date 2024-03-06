# def miFuncion():
#     print("saludos desde python")
#
#
# miFuncion()


## 72  paso de parametros

# def miFuncion(nombre,apellido):
#     print('saludos desde mi funciónn')
#     print(f'Nombre: {nombre},  Apellido: {apellido}')
#
# miFuncion('Jacobo','Valencia')

## 73 Return  en  Funciones

# def sumar(a,b):
#     #res = a + b
#     return a+b;
# #sumar(2,5)
# # res = sumar(5,3)
# # print(res)
# print(f'Resultado: {sumar(5,2)}')

## 74  Valoles pro default en los parametros

# def sumar (a = 0, b = 0) -> int:
#     return a + b
#
# resultado = sumar()
# print(f'resultado sumar:- {resultado}')
# print(f'resultado sumar: {sumar(2,8)}')

## 75  Argumenos variables en funciones

# def listarNombres(*nombres):  # se convierte en tupla  *args
#     for nombre in nombres:
#         print(nombre)
#
# listarNombres('jacobo', 'alma', 'karla', 'leslie', 'ivon' )
# listarNombres('laura','daniel')


##  76  EJERCICIO ##

def sumar_var(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_var(3,5,6))

##  78  EJERCICIO ##
def multiplicar_valore(*numeros):
    resultado = 1
    for numero in numeros:
        resultado  *= numero
    return resultado
print(multiplicar_valore(3,4,6,12))

## argumentos variables llave - valor

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Environmet')
listarTerminos(DBMS='Database Management System')

