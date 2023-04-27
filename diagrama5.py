print("diagrama comprar ingredientes para una receta")
print("inicio")
print("vas a comprar ingredientes")
print("1)si")
print("2)no")
while True:
    vascompraringredientes = input("si o no=")
    if vascompraringredientes == "1":
        print("escoger receta")
        escogerreceta = input("si=")
        if escogerreceta == "1":
            print("hacer una lista")
            hacerlista = input("si=")
            if hacerlista == "1":
                print("alistarce para salir")
                alistarseparasalir = input("si=")
                if alistarseparasalir == "1":
                    print("salir")
                    salir = input("si=")
                    if salir == "1":
                        print("dirigirse al supermercado")
                        dirigirsealsupermercado = input("si=")
                        if dirigirsealsupermercado == "1":
                            print("buscar ingredientes")
                            buscaringrediente = input("si=")
                            if buscaringrediente == "1":
                                print("hay ingredientes?")
                                hayingredientes = input("si o no=")
                                if hayingredientes == "1":
                                    print("guardar ingrediente en la cesta")     
                                    guardarinfrediente = input("si=")
                                    if guardarinfrediente == "1":
                                        print("hay otro ingrediente")
                                        hayotroingrediente = input("si o no=")
                                        if hayotroingrediente == "2":
                                            print("fin")
                                            
                                            break
                                        elif hayotroingrediente == "1":
                                            print("buscar ingediente")
                                elif hayingredientes == "2":
                                    print("buscar remplazo")
    elif vascompraringredientes == "2":
        print("fin")