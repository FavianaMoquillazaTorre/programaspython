año = int(input("Introduzca un año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("Si es una año bisiesto")
else:
    print("No es un año bisiesto")