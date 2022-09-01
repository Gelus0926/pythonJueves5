opcion=100

print("***Menu***")
print("1.Agregar Clientes: ")
print("2.Mostrar Cliente: ")
print("3.Busque un cliente por cedula")
print("4.Sacar del arreglo a un cliente")
print("0.Salir")

#LISTA
clientes=[]

while(opcion != 0):

    #Diccionario
    cliente={}

    #pedimos la opcion deseada
    opcion=int(input("digite la opcion de preferencia: "))

    #Caminos del menu
    if opcion == 1:
        cliente['cedula']=input("Digite su cedula: ")
        cliente['nombre']=input("Digite su nombre: ")
        clientes.append(cliente)
    elif(opcion == 0):
        break
    elif(opcion == 2):
        print(clientes)
    elif(opcion == 3):
        cedulaABuscar = input("Digite la cedula: ")
        for cliente in clientes:
            if(cliente["cedula"]==cedulaABuscar):
                print(f"Cliente encontrado: {cliente['cedula']}")
            else:
                print(f'Usuario no encontrado')
    elif(opcion == 0):
        break;
    else:
        print(f"Digite una opción valida")