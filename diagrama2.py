print("diagrama cafe")
print("quieres un cafe")
print("1)si")
print("2)no")
while True:
    quierescafe = input("si o no =")
    if quierescafe == "1":
        print("sacar una olla")
        sacarolla = input("si=")
        if sacarolla == "1":
            print("colocar debajo del grifo")
            olladebajodelgrifo = input("si=")
            if olladebajodelgrifo == "1":
                print("abrir grifo")
                abrirgrifo = input("si=")
                if abrirgrifo == "1":
                    print("llenar olla de agua")
                    ollallena = input ("si=")
                    if ollallena == "1":
                        print("cerrar grifo")
                        cerrargrifo = input("si=")
                        if cerrargrifo == "1":
                            print("pasar olla a estufa")
                            pasarollaestufa = input("si=")
                            if pasarollaestufa == "1":
                                print("prender estufa")
                                prenderestufa = input("si=")
                                if prenderestufa == "1":
                                    print("poner olla en la estufa")
                                    ponerollaenlaestufa = input("si=")
                                    if ponerollaenlaestufa == "1":
                                        print("esperar a que hierva agua")
                                        elaguahirvio = input("si=")
                                        if elaguahirvio == "1":
                                            print("bajar olla") 
                                            bajarolla = input("si=")
                                            if bajarolla == "1":
                                                print("poner cafe")
                                                ponercafe = input("si=")
                                                if ponercafe == "1":
                                                    print("ponerlo en la mesa")
                                                    ponerloenlamesa = input ("si=")
                                                    if ponerloenlamesa == "1":
                                                        print("quiere azucar")
                                                        azucar  = input ("si o no =")
                                                        if azucar == "1":
                                                            print("agregar azucar")
                                                            agregarazucar = input("si=")
                                                            if agregarazucar == "1":
                                                                print("agregar tinto")
                                                                agregartinto = input ("si=")
                                                                if agregartinto == "1":
                                                                    print("sacar vaso")
                                                                    sacarvaso = input("si=")
                                                                    if sacarvaso == "1":
                                                                        print("servir")
                                                                        servir = input("si=")
                                                                        if servir == "1":
                                                                            print("disfrutar")
                                                        elif azucar == "2":
                                                            print("agregar tinto")
                                                            agregartinto = input("si=")
                                                            if agregartinto == "1":
                                                                print("sacar vaso")
    elif quierescafe == "2":
        print("fin")