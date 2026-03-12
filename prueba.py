velocidad=int(input("Ingrese la velocidad " ))
if velocidad <=60 and velocidad >0:
    print("velocidad permitida")
elif velocidad >=61 and velocidad <=80:
    print("Cometio una infraccion leve por conducir sobre el limite de velocidad")
    print("Por esa misma razon tendra una multa de $200.000")
elif velocidad >=81 and velocidad <=100:
    print("Cometio una infraccion grave por conducir sobre el limite de velocidad") 
    print("Por esa misma razon tendra una multa de $400.000")
elif velocidad >=101 and velocidad <=119:
    print("Cometio una infraccion MUY grave por conducir sobre el limite de velocidad")
    print("Por esa misma razon tendra una multa de $800.000")
elif velocidad >=120:
    print("Su vehiculo sera detenido por sobrepasar los limites")
else: print("Error, dato no valido")