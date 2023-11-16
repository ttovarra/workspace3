#Una tupla es un tipo de dato abstracto que almacena valores que no pueden ser cambiados "inmutable"

tupla1=(1,2,3,"Hola","Python",12.5,12.6)

print("Datos de tupla \n",tupla1)
print("Imprime  :",tupla1[3])
print("Imprime  :",tupla1[6])
print("Imprime  :",tupla1[3:7])

f = open ('notas.txt','wt')

#numero de alumnos a solicitar
n=0
while n < 1 :
    n=int(input("Cuantos alumnos desea ingresar:  "))
#while  n > 0 :
    #ingresar los datos
    matricula=input("Captura matricula del alumno:")
    cali1=float(input("Captura calificacion 1 :"))
    cali2=float(input("Captura calificacion 2 :"))
    
    promedio=(cali1+cali2)/2
    
    print(matricula,promedio,file=f)
    n=n-1
    
f=open('notas.txt','rt')
for linea in f:
    print(linea, end='')
    
f.close
