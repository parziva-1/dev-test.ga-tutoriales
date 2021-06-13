import os, time

def clear():
    os.system("clear")
def menu():
    print("................::::INVENTARIO::::................")
    print("*" * 50)
    print("Selecciona una opción:")
    print("[C]rear producto")
    print("[L]istar todos los productos")
    print("[M]odificar un producto")
    print("[E]liminar un producto")
    print("[B]usacar un producto")
    print("[S]alir")
    print("*" * 50)

def main():
    clear()
    menu()
    command = input(">> ")
    command = command.upper().strip()

    if command == 'C':
        nombre=input("Nombre del producto a crear: ")
        stock=input("Ingresa las existencias del producto: ")
        precio=input("Ingresa el valor del producto: ")
        crear(nombre, stock, precio)

    elif command == 'L':
        listar()
    elif command == 'M':
        nombre = input("Ingrese el nombre del producto a modificar: ")
        modificar(nombre)
    elif command == 'E':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar(nombre)
    elif command == 'B':
        nombre = input("Ingrese el nombre del producto a buscar: ")
        buscar(nombre)
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        main()

def crear(nombre, stock, precio):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
 
    if nombre+"\n" in lineas:
        print("Este producto ya esta en el inventario")
        time.sleep(2)
        main()
    else:
        f = open("inventario.txt", "w")
        lineas.append(nombre)
        lineas.append(stock)
        lineas.append(precio)
        for linea in lineas:
            f.write(str(linea.strip()+"\n"))
        f.close()
        print("Producto agregado exitosamente.")
        time.sleep(2)
        main()

def listar():
    clear()
    print("................::::INVENTARIO::::................")
    print("*" * 50)
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if lineas == []:
        print("No hay productos...")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            print(linea.strip("\n"))

        while True:
            regresar = input("[R]egresar: ")
            regresar = regresar.upper().strip()
            if regresar == "R":
                main()

def modificar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            if linea == nombre+"\n":
                indice = lineas.index(linea)
                
                while True:
                    print(f"[N]ombre: {lineas[indice].strip()}, [E]xistencias: {lineas[indice+1].strip()}, [P]recio: {lineas[indice+2].strip()}, [S]alir al menu principal")
                    comando = input("Que quieres modificar: ")
                    comando = comando.upper().strip()
                    existencias, precio = None, None
                    if comando == "N":
                        nombre = input("Nombre del producto: ")+"\n"
                        lineas[indice] = nombre
                    elif comando == "E":
                        existencias = input("Canditad de existencias del producto: ")+"\n"
                        lineas[indice+1] = existencias
                    elif comando == "P":
                        precio = input("precio del producto: ")+"\n"
                        lineas[indice+2] = precio
                    elif comando == "S":
                        if lineas[indice] == nombre or lineas[indice+1] != existencias or lineas[indice+2] != precio:
                            f = open("inventario.txt", "w")
                            for linea in lineas:
                                f.write(str(linea))
                            f.close()
                            print("Producto modificado exitosamente.")
                            time.sleep(2)
                            main()
                        else:
                            main()
                    else:
                        print("Comando no valido")

def eliminar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            if linea == nombre+"\n":
                indice = lineas.index(linea)
                
                while True:
                    print(f"Nombre: {lineas[indice].strip()}, Existencias: {lineas[indice+1].strip()}, Precio: {lineas[indice+2].strip()}")
                    comando = input("Escribe [SI] para elimiar este producto o [NO] para regresar al menu principal: ")
                    comando = comando.upper().strip()

                    if comando == "SI" or comando == "S":
                        lineas.pop(indice+2)
                        lineas.pop(indice+1)
                        lineas.pop(indice)
                        f = open("inventario.txt", "w")
                        for linea in lineas:
                            f.write(str(linea.strip()+"\n"))
                        f.close()
                        print("Producto Eliminado exitosamente.")
                        time.sleep(2)
                        main()
                    elif comando == "No" or comando == "N":
                        main()
                    else:
                        print("Comando no valido")

def buscar(nombre):
    clear()
    lineas=[]
    try:
        f = open("inventario.txt", "r")
        lineas = f.readlines()
        f.close()
    except:
        f = open("inventario.txt", "w")
    if nombre+"\n" not in lineas:
        print("Producto no encontrado")
        time.sleep(2)
        main()
    else:
        for linea in lineas:
            if linea == nombre+"\n":
                indice = lineas.index(linea)
                print(f"Nombre: {lineas[indice].strip()}, Existencias: {lineas[indice+1].strip()}, Precio: {lineas[indice+2].strip()}")
                while True:
                    comando = input("¿Que desea hacer?, [E]liminarlo, [M]odificarlo, [R]eguresar al menu: ")
                    comando = comando.upper().strip()

                    if comando == "E":
                        eliminar(nombre)
                    elif comando == "M":
                        modificar(nombre)
                    elif comando == "R":
                        main()
                    else:
                        print("Comando no valido")


main()
