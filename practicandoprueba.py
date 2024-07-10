import time , os ,csv 
from funcionesprueba import * 


#para poner un numero  random 





while True: 
    os.system('cls')
    print("Gas abastible")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por rut")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")
    opc = int(input("Ingrese una opcion: "))
    os.system('cls')

    if opc ==1:
        funcion_1()
    if opc ==2:
        pass
    if opc ==3:
        pass
    if opc ==4:
        pass
    else:
        print("ADIOS!, vuelva pronto")
        time.sleep(3)




