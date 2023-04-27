print("diagrama comprara boletos")
print("inicio")
print("quieres comprara boletos en linea")
print("1)si")
print("2)no")
while True:
    quierescomprarboletosenlinea = input ("si o no=")
    if quierescomprarboletosenlinea == "1":
        print("ingresa a tuboleta.com")
        ingresatuboleta = input ("si=")
        if ingresatuboleta == "1":
            print("busca la seccion de boletos")
            buscalasecciondeboletos = input ("si=")
            if buscalasecciondeboletos == "1":
                print("escoge el boleto que deseas")
                buscasboleto = input ("si=")
                if buscasboleto == "1":
                    print ("escoge la cantidad de boletos")
                    escogecantidadboletos = input ("si=")
                    if escogecantidadboletos == "1":
                        print ("paga boletos")
                        paga = input ("si=")
                        if paga == "1":
                            print("efectivo o targeta")
                            efectivotarjeta = input ("targeta o efectivo")
                            if efectivotarjeta == "1":
                                print("selecciona tagerta con la que vas a pagar")
                                seleccionatargeta = input("si=")
                                if seleccionatargeta == "1":
                                    print("diligencia datos de pagos")
                                    diligenciapago = input("si=")
                                    if diligenciapago == "1":
                                        print("finmalizar pago")
                                        finalizarpago = input("si=")
                                        if finalizarpago == "1":
                                            print("recibir boletos")
                                            print("fin")
                                            break
                            elif efectivotarjeta == "2":
                                print("paga en efectivo")
    elif quierescomprarboletosenlinea == "2":
        print("fin")