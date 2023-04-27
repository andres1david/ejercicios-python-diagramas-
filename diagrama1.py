print("diagrama huevo frito")
print("inicio")
print("quieres un huevo frito")
print("1)si")
print("2)no")
while True:
    quierehuevo = input("si o no =")
    if quierehuevo == "1":
        print("sacar sarten")
        sarten = input("si o no =")
        if sarten == "1":
            print("poner en la estufa")
            estufa = input("si o no =")
            if estufa == "1":
                print("prender fogon")
                prenderfogon = input("si o no =")
                if prenderfogon == "1":
                    print("sacar huevo")
                    sacarhuevo = input ("si o no =")
                    if sacarhuevo == "1":
                        print("echar huevo")
                        echarhuevo = input("si =")
                        if echarhuevo == "1":
                            print("tapar sarten")
                            taparsarten = input ("si o no = ")
                            if  taparsarten == "1":
                                print("esperar de 10 a 15 min")
                                esperar = input("exacto o mas = ")
                                if esperar == "1":
                                    print("disfruta")
                                    print("fin")
                                    break
                                elif esperar == "2":
                                    print("se quemo")
                                    print("reintentar")
                            elif taparsarten == "2":
                                print("no se va a coser bien")
                        elif echarhuevo == "2":
                            print("echa huevo")                    
    elif quierehuevo == "2":
        print("fin")