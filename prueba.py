def clasificar_velocidad(velocidad):
    if velocidad <= 0:
        return "Error: la velocidad debe ser mayor que 0"
    if velocidad <= 60:
        return "Velocidad permitida"
    
    infracciones = [
        (80,  "leve",     "$200.000"),
        (100, "grave",    "$400.000"),
        (119, "MUY grave","$800.000"),
    ]
    
    for limite, tipo, multa in infracciones:
        if velocidad <= limite:
            return f"Infracción {tipo}\nMotivo: exceder el límite de velocidad\nMulta: {multa}"
    
    return "Medida extrema\nEl vehículo será detenido por sobrepasar ampliamente los límites"

def pedir_velocidad():
    while True:
        try:
            return int(input("Ingrese la velocidad del vehículo (km/h): "))
        except ValueError:
            print("Error: debes ingresar un número válido.")

def main():
    velocidad = pedir_velocidad()
    print("\n--- RESULTADO ---")
    print(clasificar_velocidad(velocidad))
    print("-----------------\n")

main()
