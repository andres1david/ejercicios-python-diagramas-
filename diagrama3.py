print("diagrma reservacion en un restaurante")
print("quieres ir a un restaurante")
print("1)si")
print("2)no")
while True:
    quieresiraunrestaurante = input ("si o no=")
    if quieresiraunrestaurante == "1":
        print("prender computador")
        prendercomputador = input ("si")
        if prendercomputador == "1":
            print("entrar a google")
            entrargoogle = input("si=")
            if entrargoogle == "1":
                print("buescar retaurante")
                buscarrestaurante = input ("si=")
                if buscarrestaurante == "1":
                    print("entrar pagina wed")
                    entrarpagina = input("si=")
                    if entrarpagina == "1":
                        print("hay disponibilidad")
                        haydisponibilidad = ("si o no=")
                        if haydisponibilidad == "1":
                            print("hay mesa para dos")
                            haymesa = input("si o no=")
                            if haymesa == "1":
                                print ("hacer reserba")
                                ("fin")
                                break
                            elif haymesa == "2":
                                print("buscar otro restaurante")
                        elif haydisponibilidad == "2":
                            print("buscar otro restaurante")
    elif quieresiraunrestaurante == "2":
        print ("fin")