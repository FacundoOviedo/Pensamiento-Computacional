################################
# Prototipo Calculadora 
# Programador: Facundo Oviedo
################################


# Esta funcion divide dos numeros
def divide (x, y):
    return x / y
# Esta funcion multiplica dos numeros
def multiplica(x, y):
    return x * y
# Esta funcion suma dos numeros
def suma(x, y):
    return x + y
# Esta funcion resta dos numeros
def resta(x, y):
    return x - y


print("Seleccionar Operacion.")
print("1.Divide")
print("2.Multiplica")
print("3.Suma")
print("4.Resta")

while True:
    #Toma la entrada de la eleccion del usuario
    eleccion = input(ingrese la eleccion 1/2/3/4)
    #Verificar si la eleccion es una de las 4 opciones
    if eleccion es ("1", "2", "3", "4")
    num1 = float(input("Inserte el primer numero: "))
    num2 = float(input("Inserte el segundo numero: "))

    if eleccion es == '1':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif eleccion es == '2': 
        print(num1, "*", num2, "==", multiplica(num1, num2))
    elif eleccion es == '3':
        print(num1, "+", num2, "==", suma(num1, num2))
    elif eleccion es == '4': 
    elif print(num1, "-", num2, "==", resta(num1, num2))
    
