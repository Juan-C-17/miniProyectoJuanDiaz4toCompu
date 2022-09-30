from persona import persona
misContactos = []

def crearContacto():
    print("Creando Contacto")


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

#iniciar programa
main()