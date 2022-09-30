from persona import persona
misContactos = [persona(123,"Astrid", "Casa 1"), persona(321, "Anjely", "Casa 2")]

def crearContacto(numero, nombre, direccion):
    misContactos.append(persona(numero, nombre, direccion))
    print("Contacto almacenado...")

def buscarContacto(nombre):
    if len(misContactos) == 0:
        print("La Lista se encuentra vacía, No hay contactos en la lista ---------->")
    else:
        encontrado = False
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                print("El teléfono es: ", misContactos[i].verNumero())
                print("La Dirección es: ", misContactos[i].verDireccion())
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == False:
            print("El contacto no existe dentro de su lista ------>")

def mostrarContactos():
    if len(misContactos) == 0:
        print("La Lista se encuentra vacía, No hay contactos en la lista ---------->")
    else:
        for i in range(len(misContactos)):
            print("\nNombre: ",misContactos[i].verNombre(),"\nTeléfono: ",misContactos[i].verNumero(), "\nDirección: ",misContactos[i].verDireccion(),)

def modificarContacto(nombre):
    if len(misContactos) == 0:
        print("La Lista se encuentra vacía, No hay contactos en la lista ---------->")
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                posicion = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado:
            nuevoNumero = int(input("Ingrese nuevo número: "))
            nuevoNombre = input("Ingrese el nuevo Nombre: ")
            nuevaDireccion = input("Ingrese la nueva Dirección: ")
            misContactos[posicion].modificarNumero(nuevoNumero)
            misContactos[posicion].modificarNombre(nuevoNombre)
            misContactos[posicion].modificarDireccion(nuevaDireccion)
            print("Contacto Actualizado Correctamente...")
        else:
            print("Contacto no encontrado...")

def eliminarContacto(nombre):
    if len(misContactos) == 0:
        print("La Lista se encuentra vacía, No hay contactos en la lista ---------->")
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                posicion = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado:
            misContactos.pop(posicion)
            print("Contacto Eliminado Correctamente...")
        else:
            print("Contacto no encontrado...")



def crearReporte():
    documento = open("reporteContactos.html","w")
    documento.write("<!doctype html>\n")
    documento.write("<html>\n")
    documento.write("<head>\n")
    documento.write("\t<title> Agenda 2022 </title>\n")
    documento.write("</head>\n")
    documento.write("<body bgcolor ='#d4ffe3'>\n")
    documento.write("\t<center>\n")
    documento.write("\t<h1>Mis Contactos</h1>\n")
    documento.write("<hr>")
    documento.write('\t<table border ="2">\n')
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Número de teléfono</td><td>Nombre</td><td>Dirección</td>\n")
    for i in range(len(misContactos)):
        documento.write("\t\t<tr>\n")
        documento.write("\t\t\t<td>" +misContactos[i].verNombre() +"</td><td>"+ str(misContactos[i].verNumero()) +"</td><td>" +misContactos[i].verDireccion() +"</td>")
        documento.write("\t\t</tr>\n")

    documento.write("\t\t</tr>\n")
    documento.write("</table>\n")
    documento.write("\t</center>\n")
    documento.write("</body>\n")
    documento.write("</html>")
    documento.write("")
    print("Reporte en html creado con éxito...")
def main():
    op = 0
    while op != 7:
        print("\n----------> Agenda 2022 <-------------")
        print("1. Crear Contacto")
        print("2. Buscar Contacto")
        print("3. Ver todos los Contactos")
        print("4. Modificar Contacto")
        print("5. Eliminar Contacto")
        print("6. Crear reporte en HTML")
        print("7. Finalizar el programa\n\n")
        op = int(input("Ingrese el número de opción: "))
        if op == 1:
            numero = int(input("Ingrese el numero de telefono: "))
            nombre = input("Ingrese el nombre del Contacto: ") 
            direccion = input("Ingrese la direccion: ")
            crearContacto(numero, nombre, direccion)
        elif op == 2:
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            buscarContacto(nombre)
        elif op == 3:
            mostrarContactos()
        elif op == 4:
            nombre = input("Ingrese el Nombre del contacto que desea modificar: ")
            modificarContacto(nombre)
        elif op == 5:
            nombre = input("Ingrese el Nombre del contacto que desea Eliminar: ")
            eliminarContacto(nombre)
        elif op == 6:
            crearReporte()
        elif op == 7:
            print("Progrma finalizado...")
        else:
            print("Opción inválida, por favor ingrese otra opción")

#iniciar programa
main()