from Tv import Tv
from Consola import Consola
from Bicicleta import Bicicleta
from Scooter import Scooter

lista_tvs = []
lista_consolas = []
lista_bicicletas = []
lista_scooters = []

def menu():
    opcion = '4'
    while opcion != '3':
        print('¿Que desea hacer?\n')
        print('1 Registrar producto')
        print('2 Cotizar producto')
        print('3 Detener programa\n')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1' or opcion == '2':
            funciones_programa(int(opcion))
        elif opcion == '3':
            print('Hasta la proxima')
        else:
            print('La opcion ingresada no es valida')
    
def funciones_programa(opcion:int):
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        cotizar_producto()

def registrar_producto():
    opcion = '6'
    while opcion != '5':
        print('¿Que producto desea registrar?\n')
        print('1 Tv')
        print('2 Consola')
        print('3 Bicicleta')
        print('4 Scooter')
        print('5 Cancelar\n')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1': # Registro de TV
            registrar_tv()

        elif opcion == '2': # Registro de Consola
            registrar_consola()

        elif opcion == '3': # Registro de Bicicleta
            registrar_bicicleta()

        elif opcion == '4': # Registro de Scooter
            registrar_scooter()

        elif opcion == '5': # Volver al menu
            print('Operacion cancelada')
        else:
            print('La opcion ingresada no es valida')

def registrar_tv():
    print('Registrando Tv')
    while True:
        try:
            voltaje = int(input('Ingrese el voltaje: '))
            if voltaje <= 0:
                print('El voltaje debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: Debe Ingresar un número entero valido. Intente nuevamente')
    while True:
        try:
            precio = float(input('Ingrese el precio: '))
            if precio <= 0:
                print('El precio debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        eficiencia = input('Ingrese letra de nivel de eficiencia: ')
        if len(eficiencia) == 1 and eficiencia.isalpha():
            break
        else:
            print('Debe ingresar una letra. Intente nuevamente')
    marca = input('Ingrese la marca: ')
    while True:
        try:
            tamanio = float(input('Ingrese el tamaño en pulgadas: '))
            if tamanio <= 0:
                print('El tamaño debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')

    tv = Tv(voltaje,precio,eficiencia,marca,tamanio)
    lista_tvs.append(tv)
    #print(f'\n {tv}')
    print('\nTv registrada\n')

def registrar_consola():
    print('Registrando Consola')
    while True:
        try:
            voltaje = int(input('Ingrese el voltaje: '))
            if voltaje <= 0:
                print('El voltaje debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: Debe Ingresar un número entero valido. Intente nuevamente')
    while True:
        try:
            precio = float(input('Ingrese el precio: '))
            if precio <= 0:
                print('El precio debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        eficiencia = input('Ingrese letra de nivel de eficiencia: ')
        if len(eficiencia) == 1 and eficiencia.isalpha():
            break
        else:
            print('Debe ingresar una letra. Intente nuevamente')
    marca = input('Ingrese la marca: ')
    nombre_consola = input('Ingrese nombre de la consola: ')
    version = ''
    while True:
        print('Seleccione version\n')
        print('1 Lite')
        print('2 Normal\n')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            version = 'Lite'
            break

        elif opcion == '2':
            version = 'Normal'
            break
        else:
            print('La opcion ingresada no es valida')

    consola = Consola(voltaje,precio,eficiencia,marca,nombre_consola,version)
    lista_consolas.append(consola)
    #print(f'\n {consola}')
    print('\nConsola registrada\n')

def registrar_bicicleta():
    print('Registrando Bicicleta')
    while True:
        try:
            aro = float(input('Ingrese el grosor del aro (milimetros): '))
            if aro <= 0:
                print('El aro debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        try:
            peso = float(input('Ingrese el peso (kg): '))
            if peso <= 0:
                print('El peso debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        try:
            precio = float(input('Ingrese el precio: '))
            if precio <= 0:
                print('El precio debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    marca = input('Ingrese la marca: ')

    bicicleta = Bicicleta(aro,peso,precio,marca)
    lista_bicicletas.append(bicicleta)
    #print(f'\n {bicicleta}')
    print('\nBicicleta registrada\n')

def registrar_scooter():
    print('Registrando Scooter')
    while True:
        try:
            voltaje = int(input('Ingrese el voltaje: '))
            if voltaje <= 0:
                print('El voltaje debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: Debe Ingresar un número entero valido. Intente nuevamente')
    while True:
        try:
            precio = float(input('Ingrese el precio: '))
            if precio <= 0:
                print('El precio debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        eficiencia = input('Ingrese letra de nivel de eficiencia: ')
        if len(eficiencia) == 1 and eficiencia.isalpha():
            break
        else:
            print('Debe ingresar una letra. Intente nuevamente')
    marca = input('Ingrese la marca: ')
    while True:
        try:
            aro = float(input('Ingrese el grosor del aro (milimetros): '))
            if aro <= 0:
                print('El aro debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        try:
            peso = float(input('Ingrese el peso (kg): '))
            if peso <= 0:
                print('El peso debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: El valor ingresado debe ser numerico. Intente nuevamente')
    while True:
        try:
            velocidad = int(input('Ingrese la velocidad (km/h): '))
            if velocidad <= 0:
                print('La velocidad debe ser mayor a 0. Intente nuevamente')
            else:
                break
        except ValueError:
            print('Error: Debe Ingresar un número entero valido. Intente nuevamente')

    scooter = Scooter(voltaje,precio,eficiencia,marca,aro,peso,velocidad)
    lista_scooters.append(scooter)
    #print(f'\n {scooter}')
    print('\nScooter registrado\n')

#def ver_productos():
#    print('Estos son los productos registrados')
#    print('\nTVs\n')
#    for tv in lista_tvs:
#        print(f'{tv}\n')

#    print('\nConsolas\n')
#    for consola in lista_consolas:
#        print(consola)

#    print('\nBicicletas\n')
#    for bicicleta in lista_bicicletas:
#        print(bicicleta)

#    print('\nScooters\n')
#    for scooter in lista_scooters:
#        print(scooter)

def cotizar_producto():
    opcion = '6'
    while opcion != '5':
        print('¿Que productos desea cotizar?\n')
        print('1 Tvs')
        print('2 Consolas')
        print('3 Bicicletas')
        print('4 Scooters')
        print('5 Cancelar\n')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            cotizar_tvs()

        elif opcion == '2':
            cotizar_consolas()

        elif opcion == '3':
            cotizar_bicicletas()

        elif opcion == '4':
            cotizar_scooters()

        elif opcion == '5':
            print('Operacion cancelada')

        else:
            print('La opcion ingresada no es valida')

def cotizar_tvs():
    print('\nTVs')
    for tv in lista_tvs:
        tv.calcular_descuento()
        print(f'\n{tv}')

def cotizar_consolas():
    print('\nConsolas')
    for consola in lista_consolas:
        consola.calcular_descuento()
        print(f'\n{consola}')

def cotizar_bicicletas():
    print('\nBicicletas')
    for bicicleta in lista_bicicletas:
        bicicleta.calcular_despacho()
        print(f'\n{bicicleta}')

def cotizar_scooters():
    print('\nScooters')
    for scooter in lista_scooters:
        scooter.calcular_descuento()
        scooter.calcular_despacho()
        print(f'\n{scooter}')

menu()