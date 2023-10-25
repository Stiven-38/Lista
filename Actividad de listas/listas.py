# Crear listas vacías
aprendices = []
edades = []

# Llenar las listas solicitando los nombres y las edades de los aprendices
for i in range(30):
    nombre = input("Ingrese el nombre del aprendiz: ")
    edad = int(input("Ingrese la edad del aprendiz: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprime la lista de los aprendices con sus edades
print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

# Obtener el aprendiz con la mayor edad
mayor_edad = edades.index(max(edades))
aprendiz_mayor_edad = aprendices[mayor_edad]
print("El aprendiz con mayor edad es:", aprendiz_mayor_edad)

# Insertar el nombre de la instructora en la posicion 1
instructora = "Adriana Lucia Rincon"
aprendices.insert(1, instructora)

# Contar cuantos aprendices tienen 18 años
cantidad18años = edades.count(18)
print("Cantidad de aprendices con 18 años:", cantidad18años)

# Agregar un aprendiz al final de la lista
aprendiz = "Andres"
aprendices.append(aprendiz)

# Borrar el nombre de la instructora de la lista
aprendices.remove(instructora)

# Buscar un dato en lista de aprendices 
dato_buscar = input("Ingrese un dato a buscar en la lista de aprendices: ")
if dato_buscar in aprendices:
    print(dato_buscar, "se encuentra en la lista de aprendices.")
else:
    print(dato_buscar, "no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista
print("primeros 10 aprendices:", aprendices[:10])

# Mostrar los 10 ultimos aprendices de la lista
print("Últimos 10 aprendices:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Elementos del 10 al 20:", aprendices[9:20])

