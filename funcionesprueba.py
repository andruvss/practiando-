import os , csv , time , msvcrt
comunas = ('Santiago','Pirque','La pintana')
pedidos = []

gas_5kg = 12500
gas_15kg = 25500




def funcion_1():
    print("-----------------------------")
    print("Registrar pedido del cliente: ")
    print("------------------------------")
    time.sleep(2)
    print("Porfavor ingrese los siguentes datos... ")
    time.sleep(2)
    os.system('cls')
    Rut = int(input("Ingrese rut del cliente... (Sin digito verificador y sin puntos): "))
    time.sleep(2)
    while True:
        try:
            nombre = input("Ingrese el nombre del cliente: ")
            if len(nombre.strip) >=3 and nombre.isalpha():
                break
            else:
                print("Porfavor escriba un nombre que contenga al menos 3 caracteres!")
    
    Direccion = int(input("Ingrese direccion del cliente: "))
    time.sleep(1)
    os.system('cls')

    comuna = int(input("Ingrese numero de comuna Disponible: "))
    time.sleep(1)
    os.system('cls')

 #Para que el usuario pueda agregar la cantidad y el cilindro deseado

    cantidad_cilindro15k = 0
    cantidad_cilindro5k = 0

    while True:
        print("Estos son los cilindros de gas disponibles!")
        print("1. 5KG -- 2500$")
        print("2. 15KG -- 25500$")
        print("3. Si desea continuar presione 3 , Asegurese de escoger su cilindro de Gas")

        opc2 = int(input("Indiqueme el cilindro de gas que desea llevar: "))
        if opc2 =="1":
            cantidad = input("Ingrese cuantos cilindros de 5KG va a desear: ")
            cantidad_cilindro5k += cantidad
        elif opc2 =="2":
            cantidad = input("Ingrese cuantos cilindros de 15KG va a desear")
            cantidad_cilindro15k += cantidad
        elif opc2 =="3":
            break 
        else: 
            print("ERROR! , OPCION INCORRECTA")

    total = cantidad_cilindro5k*gas_5kg + cantidad_cilindro15k*gas_15kg

    pedido = {"Rut":Rut, "Nombre":nombre, "Direccion":Direccion, "Comuna":comuna[comuna-1], "cant_5k":cantidad_cilindro5k, "cant_15k": cantidad_cilindro15k, "Total":total}
    pedidos.append(pedido)
    print("PEDIDO GUARDADO EXITOSAMENTE")












    

    





    



        
        
       

            

            

    

    

    
    








