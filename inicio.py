import imp
from persona import persona
misContactos = []

def  crearContacto():
    print('CreandoContacto')


def main():
    op = 0
    while op != 7:
        print('===========>> Agenda 2022 <<===========')
        print('1. Crear contacto')
        print('2. Buscar contacto')
        print('3. Ver Contactos ')
        print('4. Modificar Contacto')  
        print('5. Eliminar Contacto')
        print('6. Crear reporte en HTML')
        print('7. Salir del programa\n\n')
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            numero = int(input('Ingrese el numero de telefono'))
            nombre = int(input('Ingrese el nombre del contacto'))
            direccion = int(input('Ingrese la direccion del contacto'))
            crearContacto(numero, nombre, direccion)

#iniciar programa
main()