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

def listarNombres(*nombres):  # se convierte en tupla  *args
    for nombre in nombres:
        print(nombre)

listarNombres('jacobo', 'alma', 'karla', 'leslie', 'ivon' )
listarNombres('laura','daniel')





