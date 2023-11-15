#Funcion 1 con retorno y vacias

def imprimirDatosAlu():
    print("Curso Python\nBeto Tovar")
    
    
num1=int(input("Captura numero 1:"))
num2=int(input("Captura numero 2:"))


def sumaNumeros():
    return(num1+num2)

def restaNumeros():
    return(num1-num2)

def multiNumeros():
    return(num1*num2)

def diviNumeros():
    return(num1/num2)

#llamada o invocacion a funcion imprimir datos
imprimirDatosAlu()

#llamadas de las funciones return con retorno de datos
print("Suma es con fucion : ",sumaNumeros())
print("Resta es con fucion : ",restaNumeros())
print("Multiplicacion es con fucion : ",multiNumeros())
print("Division es con fucion : ",diviNumeros())