"""Ingresar por teclado la cantidad de términos a generar de la siguiente serie:
1 7 19 43 91 187 379 763 1531 3067 6139
El primer término es el 1 y cada término se genera como el doble del término anterior más 5.
Mostrar la serie por pantalla e informar la suma de los términos generados."""
n = int(input("Ingrese un número entre 1 y 11: "))
numerito = 1
suma = int()
print(numerito)
for n in range(1, n):
    numerito = numerito*2+5
    suma = numerito + suma
    print(numerito)
print("la suma es: ",suma+1)
