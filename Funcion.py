# prods=[
#     {"pendrive", 8000},
#     {"HDMI 2.1", 13000},
#     {"Disco duro1 TB", 35000},
#     {"Teclado", 15000}
# ]
# for p in prods:
#     print(f"{p[0]} = $ {p[1]}")
# prods.sort(key=lambda p:p[1])
# for p in prods:
#     print(f"{p[0]} = $ {p[1]}")












# notas=[5.6, 6.8, 4.1]
# def muestra_notas():
#     print("Notas ingresadas:")
#     for n in notas:
#         print(f" - {n}")
# def agregar_nota():
#     n=float(input("Ingrese la nota: "))
#     notas.append(n)
#     print("Nota agregada correctamente.")
# while True:
#     try:
#         print("""
# 1.- Agregar notas a la lista creada
# 2.-muestre por pantalla todas las notas ingresadas
# 3.-muestra la cantidad de notas ingresadas
# 4.-obtenga el promedio de las notas
# 5.-salir del programa""")
#         op=int(input("seleccione una opcion: "))
#         match op:
#             case 1:
#                 agregar_nota()
#             case 2:
#                 muestra_notas()
#             case 3:
#                 print(f"Cantidad de notas ingresadas: {len(notas)}")
#             case 4:
#                 print(f"Promedio de las notas: {sum(notas)/len(notas)}")
#             case 5:
#                 print("Saliendo del programa...")
#                 break
#     except ValueError as e:
#         print("Error", e)










