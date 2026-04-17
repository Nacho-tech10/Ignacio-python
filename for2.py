# num=int(input("Ingrese un numero: "))

# for i in range(10):
#     print(num, "X", i+1, "=", num*(i+1))



# Preguntar cuantas notas son y sacar el promedio de ellas



num=int(input("Cuantas notas son: "))
suma=0

for i in range(num):
    numero=int(input("Ingrese las notas: "))
    suma=suma+numero
prom=suma/num
print("EL promedio es: ", prom)

